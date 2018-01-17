from django.shortcuts import render
from datetime import datetime
from .models import Post

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
    # now return the rendered template
    return render(request, 'blog/posts.html', {'posts': posts})

def post(request, year, month, day, slug):
    post = Post.objects.filter(published_date__year=year,
                                published_date__month=month,
                                #published_date__day=day,
                                slug=slug)[0]
    return render(request, 'blog/post.html', {'post': post})
