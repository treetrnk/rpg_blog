from django.shortcuts import render
from datetime import datetime
from .models import Post

def index(request, tags='', search=''):
        print('Tags: ' + str(tags))
        print('Search: ' + str(search))
        context = {}
        context['meta'] = {
            'title': 'rpg stuff - A blog by Nathan Hare',
            'image': '/static/images/logo.png',
            'favicon': '/static/images/favicon.png',
            'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
	}
	# get the blog posts that are published
        if tags:
            tag_array = ','.join(tags)
            posts = Post.objects.filter(tags__icontains=tag_array)
            context['tags'] = tag_array 
        elif search:
            search_array = ' '.join(search)
            posts = Post.objects.filter(body__icontains=search_array)
            context['search'] = search_array 
        else:
            posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
        context['posts'] = posts
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
	return render(request, 'blog/post.html', {'post': post, 'meta': meta})

def rss(request):
    meta = {
        'title': 'rpg stuff - A blog by Nathan Hare',
        'image': '/static/images/logo.png',
        'favicon': '/static/images/favicon.png',
        'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
    }
    posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
    return render(request, 'blog/rss.xml', {'posts': posts, 'meta': meta})
