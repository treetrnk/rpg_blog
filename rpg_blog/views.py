from django.shortcuts import render
from apps.blog.models import Post

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
    return render(request, 'about.html', {'about': post, 'meta': meta}) 
