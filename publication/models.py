from django.db import models

from tag.models import Tag

from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters.html import HtmlFormatter

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
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    text = models.TextField()
#    class Meta:
#        abstract = True

    def pretty_print(self):
        return self.text
        
    def __unicode__(self):
        return self.title

class Comment(Content):
    pass

class Snippet(Content):
    def pretty_print(self):
        lexer = guess_lexer(self.text)
        formatter = HtmlFormatter(linenos=True, cssclass="default")
        result = highlight(self.text, lexer, formatter)
        return result

class URL(Content):
    url = models.URLField()

    
