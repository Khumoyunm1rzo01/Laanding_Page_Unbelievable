# Generated by Django 4.0.1 on 2022-06-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0040_me_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='RealClients/')),
            ],
        ),
    ]