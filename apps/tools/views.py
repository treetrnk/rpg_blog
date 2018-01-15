from django.conf import settings
from django.shortcuts import render
import os

# Create your views here.
def umdaar(request):
    return render(request, 'tools/umdaar.html')

def storygen(request):
    root_dir = os.path.dirname(settings.BASE_DIR)
    icon_dir = os.path.join(root_dir, 'apps/tools/static/tools/images/storygen')
    icons = os.listdir(icon_dir)
    return render(request, 'tools/storygen.html', {'icons': icons})

def fate_charsheet(request):
    return render(request, 'tools/fate-charsheet.html')
