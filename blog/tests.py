from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Comment, CommentVote, Post


class CommentVoteTests(TestCase):
	def setUp(self):
		self.author = User.objects.create_user("author", password="password")
		self.voter = User.objects.create_user("voter", password="password")
		self.post = Post.objects.create(
			title="Test post",
			slug="test-post",
			author=self.author,
			content="Content",
			status=1,
		)
		self.comment = Comment.objects.create(
			post=self.post,
			author=self.author,
			body="A comment",
			approved=True,
		)
		self.url = reverse(
			"comment_vote",
			args=[self.post.slug, self.comment.id, "up"],
		)

	def test_anonymous_user_cannot_vote(self):
		response = self.client.post(self.url)

		self.assertEqual(response.status_code, 302)
		self.assertFalse(CommentVote.objects.exists())

	def test_user_can_add_switch_and_remove_vote(self):
		self.client.force_login(self.voter)

		self.client.post(self.url)
		vote = CommentVote.objects.get()
		self.assertEqual(vote.value, CommentVote.UPVOTE)

		self.client.post(
			reverse("comment_vote", args=[self.post.slug, self.comment.id, "down"])
		)
		vote.refresh_from_db()
		self.assertEqual(vote.value, CommentVote.DOWNVOTE)

		self.client.post(
			reverse("comment_vote", args=[self.post.slug, self.comment.id, "down"])
		)
		self.assertFalse(CommentVote.objects.exists())
