from django.shortcuts import render
from .models import NPC
from apps.blog.models import Tag

def npcs(request, letter='A', slug=''):
    context = {}
    if len(letter) > 1:
        context["tag"] = letter.lower()
    context["letter"] = letter.title()
    alphabet = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z',
    ]

    context["alphabet"] = "<h2 class='text-center'>";
    for cletter in alphabet:
        exists = NPC.objects.filter(title__startswith=cletter).filter(published=True)
        if exists: 
            context["alphabet"] += "<a href='/npc/" + cletter + "'>" + cletter + "</a> &nbsp;"
        else:
            context["alphabet"] += cletter + " &nbsp;"
    context["alphabet"] += "</h2>"

    if context["tag"]:
        npcs = NPC.objects.filter(tags__name__in=[letter]).filter(published=True).order_by("title")
    else: 
        npcs = NPC.objects.filter(title__startswith=letter).filter(published=True).order_by("title")
    context["npcs"] = npcs
    try:
        context["selected"] = NPC.objects.get(slug=slug)
    except:
        context["selected"] = ''

    context["meta"] = {
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
    context["tags"] = Tag.objects.all().order_by('name')
    return render(request, 'beastiary/list.html', context)

def tag(request, tag):
    context = {}
    context["tag"] = tag.lower()
    alphabet = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z',
    ]

    context["alphabet"] = "<h2 class='text-center'>";
    for cletter in alphabet:
        exists = NPC.objects.filter(title__startswith=cletter).filter(published=True)
        if exists: 
            context["alphabet"] += "<a href='/npc/" + cletter + "'>" + cletter + "</a> &nbsp;"
        else:
            context["alphabet"] += cletter + " &nbsp;"
    context["alphabet"] += "</h2>"

    npcs = NPC.objects.filter(tags__name__in=[tag]).filter(published=True).order_by("title")
    context["npcs"] = npcs
    context["selected"] = ''

    context["meta"] = {
        'title': 'NPCs (' + str(tag) + ') - rpg stuff',
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
    context["tags"] = Tag.objects.all().order_by('name')
    return render(request, 'beastiary/list.html', context)
