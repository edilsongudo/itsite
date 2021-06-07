from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class ApplyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(default='')
    linkedin_url = models.CharField(
        max_length=100, blank=True, null=True)
    github_url = models.CharField(max_length=100, blank=True, null=True)
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


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=False, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
