from django.contrib import admin
from .models import Post,Tag,Image
from django.utils.html import format_html
from datetime import datetime
import hashlib

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_url', 'banner', 'get_banner', 'user', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    def get_banner(self, obj):
        return format_html(
                '<a href="{}" target="banner">{}</a>',
                str(obj.banner_url()),
                str(obj.banner_url())
        )
    get_banner.short_description = 'Banner Path'
    get_banner.admin_order_field = "banner"

    def get_url(self, obj):
        return format_html(
                '<a href="{}" target="post">{}</a>',
                '/' + str(obj.published_date.year) + '/' + 
                    str(obj.published_date.month) + '/' + 
                    str(obj.published_date.day) + '/' + 
                    obj.slug + '?code=' + obj.code(),
                'View Post'
        )
    get_url.short_description = 'URL'
    get_url.admin_order_field = "published_date"

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
