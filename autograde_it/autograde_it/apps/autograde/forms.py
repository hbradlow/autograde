from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext

from autograde.models import *
from autograde.utils import *

class ProjectForm(forms.ModelForm):
    zip_file = forms.FileField()
    def save(self,*args,**kwargs):
        self.instance = extract_from_zip(self.cleaned_data["zip_file"])
    class Meta:
        model = Project
        fields = tuple()
