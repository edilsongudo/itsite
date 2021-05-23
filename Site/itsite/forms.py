from django import forms
from .models import *
from django.forms.widgets import TextInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# class ContactForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)
#     document = forms.FileField()


class ApplyForm(forms.ModelForm):

    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial="BR"))

    class Meta:
        model = ApplyModel
        fields = '__all__'
        exclude = ['date_submited']

    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.html_name == 'phone':
                visible.field.widget.attrs['class'] = 'form-control'
