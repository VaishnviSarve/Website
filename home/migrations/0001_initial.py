# Generated by Django 4.1.5 on 2023-04-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=212)),
                ('lastname', models.CharField(max_length=212)),
                ('password', models.CharField(max_length=212)),
                ('mobileno', models.CharField(max_length=212)),
                ('address', models.CharField(max_length=212)),
                ('city', models.CharField(max_length=212)),
                ('state', models.CharField(max_length=212)),
                ('pincode', models.CharField(max_length=212)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=212)),
            ],
        ),
    ]
