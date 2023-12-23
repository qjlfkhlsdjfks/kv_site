from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    color = models.CharField(max_length=10, default='#a74d47')
    is_online = models.BooleanField(null=True)
    address = models.CharField(max_length=60, null=True)
    img = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        if self.is_online:
            return f'{self.name} | Online'
        else:
            return f'{self.name} | Offline'


class ContactUs(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField()
    comments = models.TextField()