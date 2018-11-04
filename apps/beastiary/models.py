from django.db import models
from django.contrib.auth.models import User
from apps.blog.models import Tag, Image
import markdown

# Create your models here.
class NPC(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    summary = models.TextField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=20000, blank=True, null=True)
    aspects = models.TextField(max_length=20000, blank=True, null=True)
    attributes = models.TextField(max_length=20000, blank=True, null=True)
    stunts = models.TextField(max_length=20000, blank=True, null=True)
    uses = models.TextField(max_length=20000, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.URLField(blank=True, null=True)
    image_src = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, models.PROTECT)
    edit_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def html_description(self):
        return markdown.markdown(self.description)

    def html_aspects(self):
        return markdown.markdown(self.aspects)

    def html_attributes(self):
        return markdown.markdown(self.attributes)

    def html_stunts(self):
        return markdown.markdown(self.stunts)

    def html_uses(self):
        return markdown.markdown(self.uses)

    def next_post(self):
        return self.get_next_by_title()

    def previous_post(self):
        return self.get_previous_by_title()

    def first_letter(self):
        return self.title[0].upper()

    def url(self):
        return '/npc/' + self.title[0] + '/' + self.slug

    def clean_description(self):
        pattern = '(?:\<[\s\S]*?\>)|(?:\!\[[\s\S]*?\]\([\s\S]*?\))|\#|\*|(?:\[)|(?:\]\([\s\S]*?\))|(?:[\n\r]{2,})'
        return re.sub(pattern, '', self.description)

    def is_published(self):
        if self.published_date <= timezone.now():
            return True
        else:
            return False

    def meta_summary(self):
        if self.summary is None or not self.summary:
            return self.clean_description()[0:295] + '...'
        return self.summary + '...'

    def code(self):
        return hashlib.sha512(str(self.slug + 
            str(datetime.now().month) + 
            str(datetime.now().day)).encode('utf-8')).hexdigest()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
