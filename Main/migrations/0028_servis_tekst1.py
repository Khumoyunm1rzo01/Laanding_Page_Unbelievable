# Generated by Django 4.0.1 on 2022-02-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_easy'),
    ]

    operations = [
        migrations.AddField(
            model_name='servis',
            name='tekst1',
            field=models.CharField(default=2, max_length=355),
            preserve_default=False,
        ),
    ]
