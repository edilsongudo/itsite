from django.urls import path
from itsite.views import *

urlpatterns = [
    path('', home, name="home"),
    path('apply/', apply, name="apply"),
    path('thankyou/', thankyou, name="thankyou"),
]
