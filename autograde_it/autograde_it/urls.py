from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.conf.urls import patterns, include, url
from django.shortcuts import redirect

from django.contrib import admin
import autograde.urls
import example_project.urls
from django.conf import settings
admin.autodiscover()
from django.contrib.auth.models import User

urlpatterns = patterns('',
    # Examples:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
    }),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(autograde.urls)),
    url(r'^autograde/', include(autograde.urls)),
    url(r'^users/', ListView.as_view(model=User,template_name="user_list.html"),name="users"),

    url(r'^p/',include(example_project.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
