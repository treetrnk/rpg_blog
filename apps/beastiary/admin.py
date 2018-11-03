from django.contrib import admin
from django.utils.html import format_html
from .models import NPC

class NPCAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_url', 'banner', 'user', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    def get_url(self, obj):
        return format_html(
                '<a href="{}" target="post">{}</a>',
                '/npc/' + obj.title[0] + '/' + obj.slug + '/',
                'View Post'
        )
    get_url.short_description = 'URL'

# Register your models here.
admin.site.register(NPC, NPCAdmin)
