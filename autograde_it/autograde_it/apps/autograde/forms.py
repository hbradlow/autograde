from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from django.forms.widgets import SplitDateTimeWidget,DateTimeInput

from autograde.models import *
from autograde.utils import *

class ProjectMetaForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProjectMetaForm,self).__init__(*args,**kwargs)
        self.fields['due_date'].widget = SplitDateTimeWidget()
        self.fields['release_date'].widget = SplitDateTimeWidget()
    class Meta:
        model = ProjectMeta
        exclude = ("project",)
class ProjectCreateForm(forms.ModelForm):
    def save(self,*args,**kwargs):
        super(ProjectCreateForm,self).save(*args,**kwargs)
        ProjectMeta.objects.create(project=self.instance)
    class Meta:
        model = Project
        exclude = ("instructors",)

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ("file","expected_results",)
class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ("file","is_student_viewable")
