# Generated by Django 4.0.4 on 2022-06-04 20:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_profilemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileModel',
            new_name='Profile',
        ),
    ]
