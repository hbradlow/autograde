from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext

from autograde.models import *
from autograde.utils import *

class ProjectCreateForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        if len(args)>=2:
            self.test_cases = args[1].getlist("test_cases",[])
            self.project_files = args[1].getlist("project_files",[])
        super(ProjectCreateForm,self).__init__(*args,**kwargs)
    def save(self,*args,**kwargs):
        super(ProjectCreateForm,self).save(*args,**kwargs)

        #save the files
        p = self.instance
        for test in self.test_cases:
            TestCase.objects.create(project=p, file=test)
        for file in self.project_files:
            ProjectFile.objects.create(project=p, file=file)
    class Meta:
        model = Project
        fields = ("title",)

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ("file",)
class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ("file","is_student_viewable")
