from django.contrib import admin
from django.urls import path, include

from space.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('space.urls', namespace='space')),
    path('user/', include('users.urls', namespace='users')),
]
