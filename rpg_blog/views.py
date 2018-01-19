from django.shortcuts import render
from apps.blog.models import Post

def index(request):
    return render(request, 'index.html') 

def about(request):
    post = Post.objects.filter(published_date__year=2500, slug='about')[0]
    return render(request, 'about.html', {'about': post}) 
