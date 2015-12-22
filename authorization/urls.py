from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', 'authorization.views.login'),
    url(r'^logout/$', 'authorization.views.logout'),
]
