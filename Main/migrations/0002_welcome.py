# Generated by Django 4.0.1 on 2022-02-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hello', models.CharField(max_length=255)),
            ],
        ),
    ]
