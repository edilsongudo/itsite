from django import forms
from .models import *
from django.forms.widgets import TextInput


# class ContactForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)
#     document = forms.FileField()


class ApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyModel
        fields = '__all__'
        exclude = ['date_submited']
