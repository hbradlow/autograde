from django.conf.urls import patterns, include, url
from tastypie.api import Api
from autograde.api import *

api = Api(api_name='data')
api.register(ProjectResource())
api.register(TestCaseResource())
api.register(TestResultResource())
api.register(UserResource())

urlpatterns = patterns('',
    (r'^api/', include(api.urls)),
)
