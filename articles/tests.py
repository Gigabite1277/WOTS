from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Article


class ArticleModelTest(TestCase):
    def test_article_str(self):
        article = Article(title='Test Article', slug='test-article', body='Body text.')
        self.assertEqual(str(article), 'Test Article')

    def test_article_default_is_published(self):
        article = Article(title='Draft', slug='draft', body='Body.')
        self.assertTrue(article.is_published)

    def test_article_ordering(self):
        Article.objects.create(
            title='Older Article', slug='older-article', body='Old.',
            published_date=timezone.now() - timezone.timedelta(days=2),
        )
        Article.objects.create(
            title='Newer Article', slug='newer-article', body='New.',
            published_date=timezone.now(),
        )
        articles = list(Article.objects.all())
        self.assertEqual(articles[0].title, 'Newer Article')
        self.assertEqual(articles[1].title, 'Older Article')


class HomepageViewTest(TestCase):
    def setUp(self):
        self.published = Article.objects.create(
            title='Published Article',
            slug='published-article',
            author='Alice',
            excerpt='A published excerpt.',
            body='Published body text.',
            is_published=True,
        )
        self.unpublished = Article.objects.create(
            title='Unpublished Article',
            slug='unpublished-article',
            author='Bob',
            body='Draft body text.',
            is_published=False,
        )

    def test_homepage_status_200(self):
        response = self.client.get(reverse('articles:homepage'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('articles:homepage'))
        self.assertTemplateUsed(response, 'articles/homepage.html')

    def test_homepage_shows_published_articles(self):
        response = self.client.get(reverse('articles:homepage'))
        self.assertContains(response, 'Published Article')

    def test_homepage_hides_unpublished_articles(self):
        response = self.client.get(reverse('articles:homepage'))
        self.assertNotContains(response, 'Unpublished Article')

    def test_homepage_articles_in_context(self):
        response = self.client.get(reverse('articles:homepage'))
        self.assertIn('articles', response.context)
        self.assertEqual(list(response.context['articles']), [self.published])

    def test_homepage_empty_state(self):
        Article.objects.all().delete()
        response = self.client.get(reverse('articles:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No articles have been published yet')

    def test_homepage_articles_ordered_by_most_recent(self):
        Article.objects.create(
            title='Older Post', slug='older-post', body='Old.',
            published_date=timezone.now() - timezone.timedelta(days=5),
            is_published=True,
        )
        response = self.client.get(reverse('articles:homepage'))
        articles = list(response.context['articles'])
        for i in range(len(articles) - 1):
            self.assertGreaterEqual(articles[i].published_date, articles[i + 1].published_date)


class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Detail Article',
            slug='detail-article',
            author='Carol',
            excerpt='Detail excerpt.',
            body='Full article body here.',
            is_published=True,
        )
        self.unpublished = Article.objects.create(
            title='Hidden Article',
            slug='hidden-article',
            body='Hidden.',
            is_published=False,
        )

    def test_article_detail_status_200(self):
        url = reverse('articles:article_detail', kwargs={'slug': self.article.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_uses_correct_template(self):
        url = reverse('articles:article_detail', kwargs={'slug': self.article.slug})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'articles/article_detail.html')

    def test_article_detail_shows_content(self):
        url = reverse('articles:article_detail', kwargs={'slug': self.article.slug})
        response = self.client.get(url)
        self.assertContains(response, 'Detail Article')
        self.assertContains(response, 'Full article body here.')

    def test_unpublished_article_returns_404(self):
        url = reverse('articles:article_detail', kwargs={'slug': self.unpublished.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
