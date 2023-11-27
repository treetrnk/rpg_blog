from django.urls import re_path
from . import views

urlpatterns = [
    re_path('mastersofumdaar/', views.umdaar, name='umdaar'),
    re_path('storygen/', views.storygen, name='storygen'),
    re_path('fate-charsheet/', views.fate_charsheet, name='fate_charsheet'),
]

