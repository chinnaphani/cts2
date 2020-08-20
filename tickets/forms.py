from django.forms import ModelForm
from django import forms
from .models import Engineer

# class RawEnginnerForm(forms.Form):
class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ['name',
                  'plusrid',
                  'teamname',
                  'email'
                  ]
