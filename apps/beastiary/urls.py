from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<letter>\w)\/?$', views.npcs, name='npcs-letter'),
    url(r'^(?P<letter>\w)\/(?P<slug>\S+)\/?$', views.npcs, name='npcs-specific'),
    url(r'^(?P<letter>\w+)\/?$', views.npcs, name='npcs-tag'),
    url(r'$', views.npcs, name='index'),
    #url('posts/(?P<slug>.*)', views.post, name='post'),
    #url(r'^(?:rss(?:\.xml)?)|(?:feed(?:.xml)?)$', views.rss, name='rss'),
]
