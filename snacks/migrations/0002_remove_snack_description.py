# Generated by Django 4.2.3 on 2023-07-14 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snack',
            name='description',
        ),
    ]