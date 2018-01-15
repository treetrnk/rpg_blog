from django.conf.urls import url
from . import views

urlpatterns = [
    url('mastersofumdaar/', views.umdaar, name='umdaar'),
    url('storygen/', views.storygen, name='storygen'),
    url('fate-charsheet/', views.fate_charsheet, name='fate_charsheet'),
]

