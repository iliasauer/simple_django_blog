from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authorization.urls', namespace='authorization')),
    url(r'^', include('article.urls', namespace='article')),
]
