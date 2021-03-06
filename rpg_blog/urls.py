"""rpg_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,handler404,handler500
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
#from django.urls import re_path
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about, name="about"),
    url(r'^error/$', views.handler404, name="error"),
    url(r'^beastiary/', include('apps.beastiary.urls')),
    url(r'^bestiary/', include('apps.beastiary.urls')),
    url('', include('apps.tools.urls')),
    url('', include('apps.blog.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

handler400 = views.handler404
handler403 = views.handler404
handler404 = views.handler404
handler500 = views.handler404
