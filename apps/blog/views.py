from django.shortcuts import render
from datetime import datetime
from .models import Post,Tag
import pytz
from rpg_blog.views import handler404
import hashlib

utc = pytz.UTC

def index(request):
        try:
            tag = request.GET['tag'] 
        except KeyError:
            tag = ''
        try:
            search = request.GET['search'] 
        except KeyError:
            search = ''
        print('Tags: ' + str(tag))
        print('Search: ' + str(search))
        context = {}
        context['meta'] = {
            'title': 'rpg stuff - A blog by Nathan Hare',
            'image': '/static/images/logo.png',
            'favicon': '/static/images/favicon.png',
            'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
	}
	# get the blog posts that are published
        if tag:
            #tag_array = ','.join(tags)
            posts = Post.objects.filter(tags__name__in=[tag]).filter(published_date__lte=datetime.now())
            context['searchtag'] = tag
        elif search:
            #search_array = ' '.join(search)
            posts = Post.objects.filter(body__icontains=search).filter(published_date__lte=datetime.now())
            context['search'] = search 
        else:
            posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
        context['posts'] = posts
        context['tags'] = Tag.objects.all().order_by('name')
	# now return the rendered template
        return render(request, 'blog/posts.html', context)

def post(request, year, month, day, slug):
        post = Post.objects.filter(published_date__year=year,
            published_date__month=month,
            #published_date__day=day,
            slug=slug)[0]
        meta = {
            'title': post.title + ' - rpg stuff',
            'image': str(post.banner_url()),
            'favicon': '/static/images/favicon.png',
            'description': post.description(),
        }
        tags = Tag.objects.all().order_by('name')
        if post.published_date <= utc.localize(datetime.now()):
            return render(request, 'blog/post.html', {'post': post, 'meta': meta, 'tags': tags})
        elif hasattr(request.GET, 'code'):
            if request.GET['code'].digest() == hashlib.sha512(post.slug + str(datetime.now().month()) + str(datetime.now().day())).digest():
                return render(request, 'blog/post.html', {'post': post, 'meta': meta, 'tags': tags})
            else:
                return handler404(request)
        else:
            return handler404(request)

def rss(request):
    meta = {
        'title': 'rpg stuff - A blog by Nathan Hare',
        'image': '/static/images/logo.png',
        'favicon': '/static/images/favicon.png',
        'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
    }
    posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
    return render(request, 'blog/rss.xml', {'posts': posts, 'meta': meta})
