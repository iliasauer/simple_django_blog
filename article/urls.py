from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'article.views.index'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>[0-9]+)$', 'article.views.article'),
]