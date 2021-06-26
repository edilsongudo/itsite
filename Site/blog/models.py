from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from uuslug import uuslug


class BlogPost(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="thumbs")
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=False, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(BlogPost, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
