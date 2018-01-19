from django.contrib import admin
from .models import Post,Tag,Image

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'banner', 'get_banner', 'user', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    def get_banner(self, obj):
        return obj.banner.file
    get_banner.short_description = 'Banner'

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
