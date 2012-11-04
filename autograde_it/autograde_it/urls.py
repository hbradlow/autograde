from django.conf.urls import patterns, include, url

from django.contrib import admin
import autograde.urls
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'autograde.views.upload_form', name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
    }),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autograde/', include(autograde.urls)),
)
