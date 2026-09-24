from django.db import models
from django.contrib.auth.models import User # Import models to connect
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


class CommentVote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VALUE_CHOICES = ((UPVOTE, "Upvote"), (DOWNVOTE, "Downvote"))

    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="votes"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_votes"
    )
    value = models.SmallIntegerField(choices=VALUE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("comment", "user"), name="unique_comment_vote"
            )
        ]
