# Generated by Django 4.0.1 on 2022-02-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jamoa', models.CharField(max_length=255)),
            ],
        ),
    ]
