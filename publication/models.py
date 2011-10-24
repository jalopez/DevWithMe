from django.db import models
from user_profile.models import UserProfile
from tag.models import Tag

class Publication(models.Model):
    isPublic = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    reply_to_pub = models.ForeignKey('self', null=True)
    content = models.OneToOneField('Content')
    to = models.ManyToManyField(UserProfile, null=True)

class Content(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True)
#    class Meta:
#        abstract = True

class Comment(Content):
    text = models.TextField()

class Snippet(Content):
    code = models.TextField()

class URL(Content):
    url = models.URLField()
    text = models.TextField()

    
