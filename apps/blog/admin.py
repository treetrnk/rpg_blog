from django.contrib import admin
from .models import Post,Tag,Image

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'banner', 'user', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
