from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.html import mark_safe
from markdown import markdown

# tutorial models

class Article(models.Model):
    title = models.CharField(max_length=50 , unique = True)
    subject = models.CharField(max_length=100)
    shortdesc = models.CharField(null=True , max_length=1000)
    document = models.FileField(null=True,upload_to='documents/')
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Readarticle(models.Model):
    title = models.ForeignKey(Article ,null=True, on_delete = models.CASCADE , related_name='r_title')
    description = models.TextField(null=True)
    written_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(null=True)
    written_by = models.ForeignKey(User ,null=True, on_delete = models.CASCADE , related_name='r_commented_by')
    updated_by = models.ForeignKey(User , null=True,  on_delete = models.CASCADE , related_name='r_updated_by')

    @property
    def subject_other(self):
        return self.title.subject

    @property
    def document_other(self):
        return self.title.document

    @property
    def view_other(self):
        return self.title.views
    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))

class Author(models.Model):
    blogger = models.ForeignKey(User ,null = True, on_delete = models.CASCADE , related_name='authors')
    strong = models.CharField(max_length=40)
    document = models.FileField(null=True,upload_to='documents/')
    about_author = models.TextField(max_length=4000 , null=True)
    descriptions = models.TextField(null=True)
    def get_descriptions_as_markdown(self):
        return mark_safe(markdown(self.descriptions, safe_mode='esscape'))

class Commentblog(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Article , on_delete = models.CASCADE , related_name='topic')
    commented_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    commented_by = models.ForeignKey(User , on_delete = models.CASCADE , related_name='commented_by')
    updated_by = models.ForeignKey(User ,   on_delete = models.CASCADE , related_name='updated_by')

class Mythought(models.Model):
    blogger = models.ForeignKey(User , on_delete = models.CASCADE , related_name='blogger')
    header = models.CharField(max_length=100)
    image = models.FileField(upload_to='documents/')
    description = models.TextField(max_length=4000)
    thought_on =   models.DateTimeField()
    # views = models.PositiveIntegerField(default=0)

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='essscape'))
