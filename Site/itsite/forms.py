from django import forms
from .models import *
from django.forms.widgets import TextInput
# from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from intl_tel_input.widgets import IntlTelInputWidget
# from crispy_forms.helper import FormHelper

class ApplyForm(forms.ModelForm):

    # phone = PhoneNumberField(
    #     widget=PhoneNumberPrefixWidget(initial="BR"))

    class Meta:
        model = ApplyModel
        fields = '__all__'
        exclude = ['date_submited', 'referer']
    #     widgets = {
    #         'phone': IntlTelInputWidget()
    #     }

    # def __init__(self, *args, **kwargs):
    #     super(ApplyForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.include_media = False
        # for visible in self.visible_fields():
        #     if visible.html_name == 'phone':
        #         visible.field.widget.attrs['class'] = 'form-control'


class RequestForm(forms.ModelForm):

    # phone = PhoneNumberField(
    #     widget=PhoneNumberPrefixWidget(initial="PT"))

    class Meta:
        model = RequestModel
        fields = '__all__'
        exclude = ['date_submited', 'referer']
        # widgets = {
        #     'phone': IntlTelInputWidget()
        # }

        labels = {
            'message': 'What do you need?/Job Description'
        }

    # def __init__(self, *args, **kwargs):
    #     super(RequestForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.include_media = False
        # for visible in self.visible_fields():
        #     if visible.html_name == 'phone':
        #         visible.field.widget.attrs['class'] = 'form-control'
