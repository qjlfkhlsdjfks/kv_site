from django.urls import path
from users.views import *


app_name = 'users'

urlpatterns = [
    # auth
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]

