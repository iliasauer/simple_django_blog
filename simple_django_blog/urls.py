from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authorization.urls', namespace='authorization')),
    url(r'^blog/', include('article.urls', namespace='article')),
    url(r'^forum/', include('forum.urls', namespace='article')),
    url(r'^', include('index.urls', namespace='article')),
]
