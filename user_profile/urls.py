from django.conf.urls.defaults import patterns, url
from views import GeneralFeedView, UserFeedView

urlpatterns = patterns('views',
    url(r'^$', 'general_feed'),
    url(r'^(?P<username>\w+)$', 'user_feed')
)