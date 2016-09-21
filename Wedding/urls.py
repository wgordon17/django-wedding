from django.conf import settings
from django.conf.urls import patterns, url, static
from django.views.generic import RedirectView

urlpatterns = patterns('Wedding.views',
	url(r'^(|ceremony|reception|guest-info|wedding-party|shower)$', 'main_pages'),
	url(r'^favicon\.ico$', RedirectView.as_view(url='/static/Wedding/favicon.ico')),
)

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)