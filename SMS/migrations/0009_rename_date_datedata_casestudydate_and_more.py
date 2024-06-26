# Generated by Django 5.0.2 on 2024-05-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0008_datedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datedata',
            old_name='Date',
            new_name='CaseStudyDate',
        ),
        migrations.AddField(
            model_name='datedata',
            name='ClassDate',
            field=models.CharField(default='None', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datedata',
            name='InterviewDate',
            field=models.CharField(default='None', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datedata',
            name='MockTestDate',
            field=models.CharField(default='Null', max_length=25),
            preserve_default=False,
        ),
    ]
