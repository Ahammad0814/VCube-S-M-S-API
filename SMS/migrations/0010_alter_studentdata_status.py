# Generated by Django 5.0.2 on 2024-05-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0009_rename_date_datedata_casestudydate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='Status',
            field=models.CharField(max_length=255),
        ),
    ]
