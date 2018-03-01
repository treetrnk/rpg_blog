from django.conf import settings
from django.shortcuts import render
import os

# Create your views here.
def umdaar(request):
    return render(request, 'tools/umdaar.html')

def storygen(request):
    icon_dir = os.path.join(settings.BASE_DIR, 'apps/tools/static/tools/images/storygen')
    icons = os.listdir(icon_dir)
    return render(request, 'tools/storygen.html', {'icons': icons})

def fate_charsheet(request):
    return render(request, 'tools/fate-charsheet.html')
