from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    has_relationship = models.ManyToManyField('self', through='Relationship', symmetrical=False)
    
class Relationship(models.Model):
    RELATIONSHIP_CHOICES = (
                            (1, 'Friend'),
                            )
    origin = models.ForeignKey(UserProfile, related_name='origin')
    destination = models.ForeignKey(UserProfile, related_name='destination')
    relationship_type = models.IntegerField(choices=RELATIONSHIP_CHOICES)