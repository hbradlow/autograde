from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext

from autograde.models import *
from autograde.utils import *

class ProjectForm(forms.ModelForm):
    test_case = forms.FileField()
    def save(self,*args,**kwargs):
        super(ProjectForm,self).save(*args,**kwargs)
        p = self.instance
        test_case = TestCase.objects.create(project = p, file = self.cleaned_data['test_case'])
    class Meta:
        model = Project
        fields = ("title",)
