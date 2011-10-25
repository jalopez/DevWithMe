from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('user_profile.views',
    url(r'myfeed$', 'my_feed'),
    url(r'user$', 'add_relationship'),
    url(r'(?P<username>\w+)$', 'user_feed'),
    url(r'$', 'general_feed'),    
)