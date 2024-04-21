from django.db import models
# from main.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_moderator = models.BooleanField(default=False)
    img = models.ImageField(verbose_name='image', upload_to='images', null=True, blank=False)
    
    def __str__(self) -> str:
        return self.username

