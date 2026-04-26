from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.CharField(max_length=100, default='Staff Writer')
    excerpt = models.TextField(max_length=500, blank=True)
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
