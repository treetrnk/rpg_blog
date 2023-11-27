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
from django.urls import re_path
from django.conf.urls import include,handler404,handler500
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
#from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about/$', views.about, name="about"),
    re_path(r'^error/$', views.handler404, name="error"),
    re_path(r'^beastiary/', include('apps.beastiary.urls')),
    re_path(r'^bestiary/', include('apps.beastiary.urls')),
    re_path('', include('apps.tools.urls')),
    re_path('', include('apps.blog.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

handler400 = views.handler404
handler403 = views.handler404
handler404 = views.handler404
handler500 = views.handler404
