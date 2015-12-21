from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'article.views.index'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>[0-9]+)/$', 'article.views.article'),
    url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', 'article.views.addlike'),
    url(r'^articles/addcommentary/(?P<article_id>[0-9]+)/$', 'article.views.addcommentary'),
]
