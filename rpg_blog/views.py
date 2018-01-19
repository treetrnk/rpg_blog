from django.shortcuts import render
from apps.blog.models import Post

def index(request):
    return render(request, 'index.html') 

def about(request):
    post = Post.objects.get(slug='about')
    return render(request, 'about.html', {'about': post}) 
