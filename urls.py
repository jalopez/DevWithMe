from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^tag', include('tag.urls')),
    url(r'^publication', include('publication.urls')),
    url(r'^', include('user_profile.urls')),
    
)
