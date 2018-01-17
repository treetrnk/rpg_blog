from django.db import models
from django.contrib.auth.models import User
import pytz
import os
import markdown

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="apps/blog/static/blog/images/")

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        filename = self.file.url

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    body = models.TextField(max_length=20000)
    tags = models.ManyToManyField(Tag, blank=True)
    banner = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, models.PROTECT)
    edit_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def html_body(self):
        return markdown.markdown(self.body)

    def next_post(self):
        return self.get_next_by_published_date()

    def previous_post(self):
        return self.get_previous_by_published_date()

    def url(self):
        utc = pytz.timezone('UTC')
        year = str(self.published_date.year)
        month = str('%02d' % self.published_date.month)
        day = str('%02d' % self.published_date.day)
        return '/' + year + '/' + month + '/' + day + '/' + self.slug

    def static_banner(self):
        if self.banner is None:
            return 'blog/images/default.png'
        return 'blog/images/' + self.banner.filename()

    def __str__(self):
        return self.title
