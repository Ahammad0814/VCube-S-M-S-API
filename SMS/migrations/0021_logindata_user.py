# Generated by Django 5.0.2 on 2024-06-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0020_logindata_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindata',
            name='User',
            field=models.CharField(default='User', max_length=25),
        ),
    ]
