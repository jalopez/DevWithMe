from django.conf.urls.defaults import patterns, url
from views import GeneralFeedView, UserFeedView

urlpatterns = patterns('views',
    url(r'^$', GeneralFeedView.as_view()),
    url(r'^(?P<username>\w+)$', UserFeedView.as_view())
)