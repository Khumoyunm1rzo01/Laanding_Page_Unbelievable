# Generated by Django 4.0.1 on 2022-02-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0024_simple_text1'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerful',
            name='text2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
