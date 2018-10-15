from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin

urlpatterns = [
    url(r'^', include(('Wedding.urls', 'Wedding'))),
    url(r'^admin/', admin.site.urls),
    # Comment out before '+'
]  # + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
