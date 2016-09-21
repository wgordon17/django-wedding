from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('Wedding.urls', namespace='Wedding')),
    url(r'^admin/', include(admin.site.urls)),
    # Comment out before '+'
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
