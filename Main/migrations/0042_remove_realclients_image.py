# Generated by Django 4.0.1 on 2022-06-21 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0041_realclients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realclients',
            name='image',
        ),
    ]
