from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)
    cname = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.PositiveIntegerField(null=True)
    is_online = models.BooleanField(default=False)
    address = models.CharField(max_length=60, null=True)
    img = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
