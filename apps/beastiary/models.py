from django.db import models
from django.contrib.auth.models import User
from apps.blog.models import Tag, Image
import markdown

# Create your models here.
class NPC(models.Model):
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
        return self.get_next_by_title()

    def previous_post(self):
        return self.get_previous_by_title()

    def first_letter(self):
        return self.title[0].upper()

    def url(self):
        utc = pytz.timezone('UTC')
        year = str(self.published_date.year)
        month = str('%02d' % self.published_date.month)
        day = str('%02d' % self.published_date.day)
        return '/' + year + '/' + month + '/' + day + '/' + self.slug

    def banner_placeholder_url(self):
        return '/static/images/loading.gif'

    def banner_url(self):
        if self.banner is None:
            return '/media/default.png'
        return '/media/' + self.banner.filename()

    def clean_body(self):
        pattern = '(?:\<[\s\S]*?\>)|(?:\!\[[\s\S]*?\]\([\s\S]*?\))|\#|\*|(?:\[)|(?:\]\([\s\S]*?\))|(?:[\n\r]{2,})'
        return re.sub(pattern, '', self.body)

    def is_published(self):
        if self.published_date <= timezone.now():
            return True
        else:
            return False

    def description(self):
        if self.summary is None or not self.summary:
            return self.clean_body()[0:295] + '...'
        return self.summary + '...'

    def code(self):
        return hashlib.sha512(str(self.slug + 
            str(datetime.now().month) + 
            str(datetime.now().day)).encode('utf-8')).hexdigest()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date', 'title']
