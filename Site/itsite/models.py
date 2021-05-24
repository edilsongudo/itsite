from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class ApplyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(default='')
    linkedin_profile_url = models.URLField(
        max_length=100, blank=True, null=True)
    github_profile_url = models.URLField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to=f'cvs')
    date_submited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} cv'


class RequestModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(default='', blank=True, null=True)
    message = models.TextField()
    document = models.FileField(upload_to=f'documents', blank=True, null=True)
    date_submited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} apply'
