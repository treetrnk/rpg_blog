from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<year>\d{4})\/(?P<month>\d{1,2})\/(?P<day>\d{1,2})\/(?P<slug>\S+)$', views.post, name='post'),
    #re_path('posts/(?P<slug>.*)', views.post, name='post'),
    re_path(r'^(?:rss(?:\.xml)?)|(?:feed(?:.xml)?)$', views.rss, name='rss'),
    re_path(r'^$', views.index, name='index'),
]
