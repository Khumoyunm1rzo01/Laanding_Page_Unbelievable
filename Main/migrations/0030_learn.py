# Generated by Django 4.0.1 on 2022-02-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0029_muvaffaqiyat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organish', models.CharField(max_length=355)),
            ],
        ),
    ]
