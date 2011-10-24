from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from publication.models import Publication

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False, 
                                           null=True, blank=True)
    
    def get_feed(self):
        
        relationships = self.relationships.all()   
        publications = Publication.objects.filter(
            Q(to=self) | (Q(is_public=False)& Q(published_by__in=relationships)) |
            Q(published_by=self)
        ).filter(reply_to_pub=None).order_by('-date')
        return publications

    def __unicode__(self):
        return self.user.username
        
        


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)


class Relationship(models.Model):
    RELATIONSHIP_CHOICES = (
                            (1, 'Friend'),
                            )
    origin = models.ForeignKey(UserProfile, related_name='origin')
    destination = models.ForeignKey(UserProfile, related_name='destination')
    relationship_type = models.IntegerField(choices=RELATIONSHIP_CHOICES)
    
    def __unicode__(self):
        return "%s -> %s" % (self.origin, self.destination)
    
