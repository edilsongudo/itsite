from django.urls import path
from blog.views import *
from django.contrib.sitemaps.views import sitemap
from itsite.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('', blog, name="blog"),
    path('<str:slug>/', blogpost, name="blogpost"),
]


from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
