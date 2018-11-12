from django.shortcuts import render
from .models import NPC
from apps.blog.models import Tag,Post

def npcs(request, letter='All', slug=''):
    context = {}
    if len(letter) > 1 and letter != "All":
        context["tag"] = letter.lower()
    context["letter"] = letter.title()
    alphabet = [
        'All','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z',
    ]

    context["post"] = Post.objects.get(slug="beastiary")

    context["alphabet"] = "<h2 class='text-center'>";
    for nav_letter in alphabet:
        exists = NPC.objects.filter(title__startswith=nav_letter).filter(published=True)
        selected = "alpha-selected" if context["letter"] == nav_letter else ""
        if exists: 
            context["alphabet"] += "<a href='/beastiary/" + nav_letter + "' class='" + selected + "'>" + nav_letter + "</a> &nbsp;"
        elif nav_letter == "All":
            context["alphabet"] += "<a href='/beastiary/' class='" + selected + "'>" + nav_letter + "</a> &nbsp;"
        else:
            context["alphabet"] += "<span class='" + selected + "'>" + nav_letter + "</span> &nbsp;"
    context["alphabet"] += "</h2>"

    try:
        if letter == "All":
            npcs = NPC.objects.filter(published=True).order_by("title")
        elif context["tag"]:
            npcs = NPC.objects.filter(tags__name__in=[letter]).filter(published=True).order_by("title")
    except:
        npcs = NPC.objects.filter(title__startswith=letter).filter(published=True).order_by("title")
    context["npcs"] = npcs
    try:
        context["selected"] = NPC.objects.get(slug=slug)
    except:
        context["selected"] = ''

    context["meta"] = {
        'title': 'Beastiary (' + str(context["letter"]) + ') - rpg stuff',
        'image': '',
        'favicon': '/static/images/favicon.png',
        'description': 'A list of pregenerated NPC and monster stats to use in you Fate Core games. The list includes: ',
    }

    for npc in npcs:
        context["meta"]["description"] += npc.title + " "
    context["meta"]["description"] = context["meta"]["description"][0:296] + "..."

    context["tags"] = Tag.objects.all().order_by('name')
    return render(request, 'beastiary/list.html', context)
