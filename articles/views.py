from django.shortcuts import get_object_or_404, render

from .models import Article


def homepage(request):
    articles = Article.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'articles/homepage.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'articles/article_detail.html', {'article': article})
