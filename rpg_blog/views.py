from django.shortcuts import render
from apps.blog.models import Post,Tag

def index(request):
    return render(request, 'index.html') 

def about(request):
    post = Post.objects.get(slug='about')
    meta = {
        'title': 'rpg stuff - A blog by Nathan Hare',
        'image': '/static/images/logo.png',
        'favicon': '/static/images/favicon.png',
        'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
    }
    tags = Tag.objects.all().order_by('name')
    return render(request, 'page.html', {'page': post, 'meta': meta, 'tags': tags}) 

def handler404(request):
    post = Post.objects.get(slug='404-error')
    meta = {
        'title': 'rpg stuff - A blog by Nathan Hare',
        'image': '/static/images/logo.png',
        'favicon': '/static/images/favicon.png',
        'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
    }
    tags = Tag.objects.all().order_by('name')
    return render(request, 'page.html', {'page': post, 'meta': meta, 'tags': tags}) 
