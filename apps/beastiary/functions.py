from .models import NPC

def npc_list(letter, npc=""):
    return NPC.object.filter(title__iregex=r"^[%s%s]*" % (letter, letter.upper()))

def alphabet_links(letter="a"):

    return "a"
