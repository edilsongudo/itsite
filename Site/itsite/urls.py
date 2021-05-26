from django.urls import path
from itsite.views import *

urlpatterns = [
    path('', home, name="home"),
    path('apply/', apply, name="apply"),
    path('hire/', hire, name="hire"),
    path('thankyou/', thankyou, name="thankyou"),
    path('jobs/', jobs, name="jobs"),
    path('calc/', calculator, name="calculator"),
]


from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
