from django.shortcuts import render
from .models import NPC
from apps.blog.models import Tag

def npcs(request, letter='A', slug=''):
    context = {}
    context["letter"] = letter.upper()
    alphabet = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z',
    ]

    context["alphabet"] = "<h2 class='text-center'>";
    for cletter in alphabet:
        context["alphabet"] += "<a href='/npc/" + cletter + "'>" + cletter + "</a> &nbsp;"
    context["alphabet"] += "</h2>"

    npcs = NPC.objects.filter(title__startswith=letter).order_by("title")
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
    print(letter)
    print(npcs)
    print(context["npcs"])
    return render(request, 'beastiary/list.html', context)
