from django.db import models
from django.contrib.auth.models import User
from apps.blog.models import Tag, Image
import markdown
import re

class Stress(models.Model):
    STRESS_CHOICES = (
        ("1", "1[ ]"),        
        ("1,1", "1[ ] 1[ ]"),        
        ("1,1,1", "1[ ] 1[ ] 1[ ]"),        
        ("1,1,1,1", "1[ ] 1[ ] 1[ ] 1[ ]"),        
        ("1,2", "1[ ] 2[ ]"),        
        ("1,2,3", "1[ ] 2[ ] 3[ ]"),        
        ("1,2,3,4", "1[ ] 2[ ] 3[ ] 4[ ]"),        
    )
    boxes = models.TextField(max_length=3000)

    def html_boxes(self):
        return markdown.markdown(self.boxes)

    def clean_boxes(self):
        pattern = '(?:\<[\s\S]*?\>)|(?:\!\[[\s\S]*?\]\([\s\S]*?\))|\#|\*|(?:\[)|(?:\]\([\s\S]*?\))|(?:[\n\r]{2,})|(?:hysical)|(?:ental)|(?:tress)|(?:&nbsp;)'
        return re.sub(pattern, '', self.boxes)

    def __str__(self):
        return self.clean_boxes()

    class Meta:
        ordering = ['boxes']

class Consequence(models.Model):
    name = models.CharField(max_length=150)
    placeholder = models.CharField(max_length=150,blank=True,null=True)

    def html_form(self):
        placeholder = str(self.placeholder) if self.placeholder else ""
        output = "<div class='row'><label class='control-label text-right col-sm-2 col-xs-6'>" + str(self.name) + "</label>"
        output += "<div class='col-sm-10 col-xs-6'><input type='text' class='form-control input-sm' placeholder='" + placeholder + "' /></div></div>"
        return output

    def __str__(self):
        placeholder = " (" + self.placeholder + ")" if self.placeholder else "" 
        return self.name + placeholder

    class Meta:
        ordering = ['name','placeholder']

class NPC(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    summary = models.TextField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=20000, blank=True, null=True)
    aspects = models.TextField(max_length=20000, blank=True, null=True)
    attributes = models.TextField(max_length=20000, blank=True, null=True)
    stunts = models.TextField(max_length=20000, blank=True, null=True)
    stress = models.ForeignKey(Stress,on_delete=models.PROTECT, blank=True, null=True)
    consequences = models.ManyToManyField(Consequence, blank=True)
    uses = models.TextField(max_length=20000, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.URLField(blank=True, null=True)
    image_src = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
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

    def is_pregen(self):
        for tag in self.tags.all():
            if tag.name == "pregen":
                return True
        return False

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

