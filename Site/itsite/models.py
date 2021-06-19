from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from uuslug import uuslug


class ApplyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    full_number = models.CharField(max_length=100)
    linkedin_url = models.CharField(
        max_length=100, blank=True, null=True)
    github_url = models.CharField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to=f'cvs')
    date_submited = models.DateTimeField(default=timezone.now)
    referer = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name} cv'


class RequestModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    full_number = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    document = models.FileField(upload_to=f'documents', blank=True, null=True)
    date_submited = models.DateTimeField(default=timezone.now)
    referer = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name} apply'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=False, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
