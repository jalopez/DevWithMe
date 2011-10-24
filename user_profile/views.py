from djangorestframework.views import View
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class GeneralFeedView(View):
    def get(self, request):
        pass
    
    
class UserFeedView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username).get_profile()
        return user.get_feed()