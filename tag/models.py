from django.db import models

from publication.models import Publication

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.tag;
    
    def get_feed(self):
        publications = Publication.objects.filter(content__tags=self).filter(reply_to_pub=None).order_by("-date")
        feed = [{'pub': pub, 
                 'replies': Publication.objects.filter(reply_to_pub=pub).count()} 
                for pub in publications]
        return feed
