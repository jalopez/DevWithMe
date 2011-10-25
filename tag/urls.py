from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tag.views',
    url(r'(?P<tag>\w+)$', 'tag_feed'),    
)