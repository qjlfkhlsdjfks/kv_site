from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from space.views import *


app_name = 'space'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('museums/', museums, name='museums'),
    path('online/', onlines, name='onlines'),
    path('museums/place/id=<card_id>', place, name='place')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)