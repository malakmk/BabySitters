from django.forms import ModelForm
from django import forms
from .models import BabySitter

class BabySitterForm(forms.ModelForm):
    class Meta:
        model = BabySitter
        fields = ['Name', 'Email', 'DateOfBirth']

