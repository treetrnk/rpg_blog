from django.shortcuts import render

# Create your views here.
def umdaar(request):
    return render(request, 'tools/umdaar.html')

def storygen(request):
    return render(request, 'tools/storygen.html')

def fate_charsheet(request):
    return render(request, 'tools/fate-charsheet.html')
