from django.shortcuts import render
from .models import NPC
from apps.blog.models import Tag

def npcs(request, letter='A', slug=''):
    npcs = NPC.objects.filter(title__startswith=letter)
    try:
        selected = NPC.objects.get(slug=slug)
    except:
        selected = ''
    meta = {
        'title': 'NPCs (' + str(letter) + ') - rpg stuff',
        'image': '',
        'favicon': '/static/images/favicon.png',
        'description': 'farts',
    }
    """
    meta = {
        'title': npcs.title + ' - rpg stuff',
        'image': str(npcs.banner_url()),
        'favicon': '/static/images/favicon.png',
        'description': npcs.description(),
    }
    """
    tags = Tag.objects.all().order_by('name')
    return render(request, 'beastiary/list.html', {'letter': letter, 'npcs': npcs, 'selected': selected.title, 'meta': meta, 'tags': tags})
