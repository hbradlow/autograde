from django.conf.urls import patterns, include, url

from django.contrib import admin
from autograde.views import ProjectDetailView
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'autograde_it.views.home', name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^project/(?P<pk>[\w\._-]+)$', ProjectDetailView.as_view(), name='project_detail'),
    # url(r'^autograde_it/', include('autograde_it.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
