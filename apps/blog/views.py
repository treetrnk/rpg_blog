from django.shortcuts import render
from datetime import datetime
from .models import Post

def index(request):
	meta = {
		'title': 'rpg stuff - A blog by Nathan Hare',
		'image': '/static/images/logo.png',
		'favicon': '/static/images/favicon.png',
		'description': 'A blog by Nathan Hare about Fate Core and other roleplaying games.',
	}
	# get the blog posts that are published
	posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
	# now return the rendered template
	return render(request, 'blog/posts.html', {'posts': posts, 'meta': meta})

def post(request, year, month, day, slug):
	post = Post.objects.filter(published_date__year=year,
		published_date__month=month,
		#published_date__day=day,
		slug=slug)[0]
	meta = {
		'title': post.title + ' - rpg stuff',
		'image': str(post.banner_url),
		'favicon': '/static/images/favicon.png',
		'description': post.clean_body()[0:120] + '...',
	}
	return render(request, 'blog/post.html', {'post': post, 'meta': meta})
