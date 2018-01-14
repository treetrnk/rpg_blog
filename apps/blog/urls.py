from django.conf.urls import url
from . import views

urlpatterns = [
    url('posts/(?P<slug>.*)', views.post, name='post'),
    url(r'^$', views.index, name='index'),
]

