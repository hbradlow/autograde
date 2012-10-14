from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext

from autograde.models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ("instructor","test_cases","student_files",)
