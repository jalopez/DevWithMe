from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to

from publication.models import Publication

@render_to('feed.html')
def general_feed(request):
    publications = Publication.objects.filter(is_public=True).filter(reply_to_pub=None)
    return {'feed': publications}
    
@render_to('feed.html')  
def user_feed(request, username):
        user = get_object_or_404(User, username=username).get_profile()
        return {'feed': user.get_feed()}
