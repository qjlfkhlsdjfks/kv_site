# Generated by Django 5.0 on 2023-12-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='address',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
