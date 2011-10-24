from django.db import models

from tag.models import Tag

class Publication(models.Model):
    is_public = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    reply_to_pub = models.ForeignKey('self', null=True, blank=True)
    content = models.OneToOneField('Content')
    to = models.ManyToManyField('user_profile.UserProfile', null=True, blank=True)
    published_by = models.ForeignKey('user_profile.UserProfile', related_name='publisher')
    
    def __unicode__(self):
        return "%s on %s" % (self.published_by, self.date)

class Content(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    text = models.TextField()
#    class Meta:
#        abstract = True
    def __unicode__(self):
        return self.title

class Comment(Content):
    pass

class Snippet(Content):
    pass

class URL(Content):
    url = models.URLField()

    
