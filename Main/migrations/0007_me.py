# Generated by Django 4.0.1 on 2022-02-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_delete_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=255)),
            ],
        ),
    ]