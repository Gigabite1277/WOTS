from django.shortcuts import render, get_object_or_404, reverse
from django.conf import settings
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Post, Comment, CommentVote
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    extra_context = {"cloudinary_configured": settings.CLOUDINARY_CONFIGURED}


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.annotate(
        upvote_count=Count("votes", filter=Q(votes__value=CommentVote.UPVOTE)),
        downvote_count=Count("votes", filter=Q(votes__value=CommentVote.DOWNVOTE)),
    ).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
@require_POST
def comment_vote(request, slug, comment_id, value):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=post)
    value = {"up": CommentVote.UPVOTE, "down": CommentVote.DOWNVOTE}.get(value)

    if value not in (CommentVote.UPVOTE, CommentVote.DOWNVOTE):
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))

    vote, created = CommentVote.objects.get_or_create(
        comment=comment,
        user=request.user,
        defaults={"value": value},
    )
    if not created:
        if vote.value == value:
            vote.delete()
        else:
            vote.value = value
            vote.save(update_fields=["value"])

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

