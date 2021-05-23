from django.db import models
from django.utils import timezone


class ApplyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin_profile_url = models.URLField(max_length=100, blank=True)
    github_profile_url = models.URLField(max_length=100, blank=True)
    cv = models.FileField(upload_to=f'cvs')
    date_submited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} cv'
