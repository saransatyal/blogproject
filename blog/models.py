from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# tutorial models

class Article(models.Model):
     title = models.CharField(max_length=50 , unique = True)
     subject = models.CharField(max_length=100)
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

class Author(models.Model):
        blogger = models.ForeignKey(User ,null = True, on_delete = models.CASCADE , related_name='authors')
        strong = models.CharField(max_length=40)
        document = models.FileField(null=True,upload_to='documents/')
        about_author = models.TextField(max_length=4000 , null=True)
        long_description = models.TextField(max_length=10000 , null=True)

class Commentblog(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Article , on_delete = models.CASCADE , related_name='topic')
    commented_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    commented_by = models.ForeignKey(User , on_delete = models.CASCADE , related_name='commented_by')
    updated_by = models.ForeignKey(User ,   on_delete = models.CASCADE , related_name='updated_by')
