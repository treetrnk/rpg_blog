from django.db import models
from django.contrib.auth.models import User
import pytz
import os
import re
import markdown

# Create your models here.
class Tag(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ['name']

class Image(models.Model):
        name = models.CharField(max_length=50)
        file = models.ImageField()
        credit = models.TextField(max_length=300, blank=True, null=True)

        def filename(self):
            return os.path.basename(self.file.name)

        def file_path(self):
            return '/media/' + str(self.filename())

        def html_credit(self):
            if self.credit is not None:
                return markdown.markdown(self.credit)
            return ''

        def __str__(self):
            return self.name

        def save(self, *args, **kwargs):
            super(Image, self).save(*args, **kwargs)
            filename = self.file.url

        class Meta:
            ordering = ['name']

class Post(models.Model):
        title = models.CharField(max_length=200)
        slug = models.SlugField(max_length=200, null=True)
        summary = models.TextField(max_length=300, blank=True, null=True)
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

        def banner_url(self):
            if self.banner is None:
                return '/media/default.png'
            return '/media/' + self.banner.filename()

        def clean_body(self):
            pattern = '(?:\<[\s\S]*?\>)|(?:\!\[[\s\S]*?\]\([\s\S]*?\))|\#|\*|(?:\[)|(?:\]\([\s\S]*?\))|(?:[\n\r]{2,})'
            return re.sub(pattern, '', self.body)

        def description(self):
            if self.summary is None:
                return self.clean_body()[0:295] + '...'
            return self.summary

        def __str__(self):
            return self.title

        class Meta:
            ordering = ['-published_date', 'title']
