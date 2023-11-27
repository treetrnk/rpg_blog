from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<letter>[\w\s])\/?$', views.npcs, name='npcs-letter'),
    re_path(r'^(?P<letter>[\w\s])\/(?P<slug>\S+)\/?$', views.npcs, name='npcs-specific'),
    re_path(r'^(?P<letter>[\w\s]+)\/?$', views.npcs, name='npcs-tag'),
    re_path(r'$', views.npcs, name='index'),
    #re_path('posts/(?P<slug>.*)', views.post, name='post'),
    #re_path(r'^(?:rss(?:\.xml)?)|(?:feed(?:.xml)?)$', views.rss, name='rss'),
]
