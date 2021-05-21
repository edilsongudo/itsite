from django.urls import path
from itsite.views import *

urlpatterns = [
    path('', home, name="home"),
    path('hire/', hire, name="hire"),
]
