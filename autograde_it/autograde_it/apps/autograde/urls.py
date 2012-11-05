from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from autograde.api import *
from autograde.views import *
from autograde.models import *

api = Api(api_name='data')
api.register(ProjectResource())
api.register(TestCaseResource())
api.register(TestResultResource())
api.register(UserResource())

urlpatterns = patterns('',
    (r'^api/', include(api.urls)),

    url(r'^project/(?P<pk>[\w\._-]+)$', DetailView.as_view(model=Project), name='project_detail'),

    url(r'^testcase/(?P<pk>[\w\._-]+)$', DetailView.as_view(model=TestCase), name='testcase_detail'),
    url(r'^testcase/(?P<pk>[\w\._-]+)/edit$', testcase_edit, name='testcase_edit'),

    url(r'^projectfile/(?P<pk>[\w\._-]+)$', DetailView.as_view(model=ProjectFile), name='projectfile_detail'),
    url(r'^projectfile/(?P<pk>[\w\._-]+)/edit$', projectfile_edit, name='projectfile_edit'),

    url(r'^testresult/(?P<pk>[\w\._-]+)$', DetailView.as_view(model=TestResult), name='testresult_detail'),
)
