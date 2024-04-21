from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from space.views import *


app_name = 'space'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<category_name>/', category, name='category'),

    path('place/id=<place_id>', place, name='place'),
    path('place/rate/id=<place_id>', rate, name='rate'),
    path('category/<category_name>', category, name='category')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)