# myapp/api.py
from tastypie.resources import ModelResource
from tastypie import fields
from autograde.models import *

class TestCaseResource(ModelResource):
    class Meta:
        queryset = TestCase.objects.all()
        resource_name = 'testcase'
class ProjectResource(ModelResource):
    tests = fields.ToManyField("autograde.api.TestCaseResource","test_cases",full=True)
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
