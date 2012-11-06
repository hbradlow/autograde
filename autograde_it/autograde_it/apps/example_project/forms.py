from django import forms
from example_project.models import UserFeedback

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
