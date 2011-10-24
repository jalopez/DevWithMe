from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('user_profile.views',
    url(r'(?P<username>\w+)$', 'user_feed'),
    url(r'$', 'general_feed'),    
)