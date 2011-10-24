from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to

from publication.models import Publication

def general_feed(request):
    publications = Publication.objects.filter(is_public=True)
    return publications
    
@render_to('feed.html')  
def user_feed(request, username):
        user = get_object_or_404(User, username=username).get_profile()
        return user.get_feed()