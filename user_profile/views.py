from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from annoying.decorators import render_to
from django.http import HttpResponseForbidden


from forms import RelationshipForm
from models import Relationship
from publication.models import Publication

@render_to('feed.html')
def general_feed(request):
    publications = Publication.objects.filter(is_public=True).filter(reply_to_pub=None).order_by("-date")
    feed = [{'pub': pub, 'replies': Publication.objects.filter(reply_to_pub=pub).count()} 
            for pub in publications]
    return {'feed': feed}
    

@login_required
@render_to('feed.html')
def user_feed(request, username):
        requested_user = get_object_or_404(User, username=username).get_profile()
        logged_user =  request.user.get_profile()
        relationships = logged_user.relationships.all()
        if logged_user == requested_user or requested_user in relationships:
            return {'feed': requested_user.get_feed(), 
                    'user_feed': username                 
                    }
        else:
            return HttpResponseForbidden("You are not allowed to access this feed")
        
@login_required
def add_relationship(request):
    if request.method != 'POST':
        return HttpResponseForbidden("Method not allowed")
    next = "/"
    if (request.GET.has_key("next")):
        next = request.GET["next"]
        
    form = RelationshipForm(request.POST)
        
    if not form.is_valid():
        #add error
        return redirect(next)
    
    username = form.cleaned_data['user']
    
    followed = get_object_or_404(User, username=username).get_profile()
    
    user = request.user.get_profile()
    
    if user != followed:
        m1 = Relationship(origin=user, destination=followed, relationship_type=1)
        m1.save()
    else:
        pass
        #add error
    return redirect(next)
    
    
        
