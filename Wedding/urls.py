from django.conf import settings
from django.urls import re_path
from django.conf.urls import static
from django.views.generic import RedirectView
from .views import main_pages

urlpatterns = [
    re_path(r'^(|ceremony|reception|guest-info|wedding-party|shower)$', main_pages),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/Wedding/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
