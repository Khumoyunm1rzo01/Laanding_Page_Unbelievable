# Generated by Django 4.0.1 on 2022-06-21 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0038_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='image',
        ),
    ]
