from django.shortcuts import render
from datetime import datetime
from .models import Post

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published_date__lte=datetime.now())
    # now return the rendered template
    return render(request, 'blog/posts.html', {'posts': posts})

