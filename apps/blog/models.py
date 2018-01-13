from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    body = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    banner = models.CharField(max_length=2000, blank=True, null=True)
    user = models.ForeignKey(User, models.PROTECT)
    edit_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
