from djangorestframework.views import View
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from publication.models import Publication

class GeneralFeedView(View):
    def get(self, request):
        publications = Publication.objects.filter(is_public=True)
        return publications
    
    
class UserFeedView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username).get_profile()
        return user.get_feed()