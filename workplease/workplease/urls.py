from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from socialnet.views import *
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('socialnet.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'socialnet.views.view_404'
