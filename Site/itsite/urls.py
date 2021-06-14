from django.urls import path
from itsite.views import *
from django.contrib.sitemaps.views import sitemap
from itsite.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('', home, name="home"),
    path('apply/', apply, name="apply"),
    path('hire/', hire, name="hire"),
    path('thankyou/', thankyou, name="thankyou"),
    path('jobs/', jobs, name="jobs"),
    path('job/<str:slug>', job, name="job"),
    path('calc/', calculator, name="calculator"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
]


from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
