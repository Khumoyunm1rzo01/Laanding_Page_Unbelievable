# Generated by Django 4.0.5 on 2022-06-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0050_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_tittle', models.CharField(max_length=355)),
                ('adress_name', models.CharField(max_length=255)),
                ('call_tittle', models.CharField(max_length=255)),
                ('call_phone', models.IntegerField()),
                ('email_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
    ]
