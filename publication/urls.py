from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('publication.views',
    url(r'(?P<pub_id>\d+)$', 'publication_detail')
)