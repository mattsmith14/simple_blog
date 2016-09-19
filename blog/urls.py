from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<id>\d+)/$', views.post, name='post'),
]
