from django.contrib import admin
from .models import ApplyModel, RequestModel, Post

# Register your models here.
admin.site.register(ApplyModel)
admin.site.register(RequestModel)
admin.site.register(Post)
