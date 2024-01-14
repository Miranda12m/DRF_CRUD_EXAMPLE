from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('d0oai32492384h24uicrulabiwouej23n4k2jnkjnkjn/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html')),
    path('services/', include('api_services.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)