# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication,ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie import fields
from autograde.models import *
from django.contrib.auth.models import User

class TestResultResource(ModelResource):
    test_case = fields.ForeignKey("autograde.api.TestCaseResource","test_case")
    user = fields.ForeignKey("autograde.api.UserResource","user")
    class Meta:
        queryset = TestResult.objects.all()
        resource_name = 'test_result'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post']

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class TestCaseResource(ModelResource):
    project = fields.ForeignKey("autograde.api.ProjectResource","project")
    class Meta:
        queryset = TestCase.objects.all()
        resource_name = 'test_case'

class ProjectResource(ModelResource):
    tests = fields.ToManyField("autograde.api.TestCaseResource","testcase_set",full=True)
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
