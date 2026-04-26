from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]
