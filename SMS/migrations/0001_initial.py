# Generated by Django 5.0.2 on 2024-05-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchName', models.CharField(max_length=25)),
                ('Classes', models.IntegerField()),
                ('CaseStudies', models.IntegerField()),
                ('MockTests', models.IntegerField()),
                ('Interviews', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=25)),
                ('Password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchName', models.CharField(max_length=25)),
                ('JoiningDate', models.DateField()),
                ('Name', models.CharField(max_length=25)),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=25)),
                ('PG', models.CharField(max_length=25)),
                ('PG_Branch', models.CharField(max_length=25)),
                ('PG_CGPA', models.IntegerField()),
                ('PG_Year', models.IntegerField()),
                ('Degree', models.CharField(max_length=25)),
                ('Degree_Branch', models.CharField(max_length=25)),
                ('Degree_CGPA', models.IntegerField()),
                ('Degree_Year', models.IntegerField()),
                ('Inter', models.CharField(max_length=25)),
                ('Inter_Branch', models.CharField(max_length=25)),
                ('Inter_CGPA', models.IntegerField()),
                ('Inter_Year', models.IntegerField()),
                ('SSC', models.CharField(max_length=25)),
                ('SSC_Branch', models.CharField(max_length=25)),
                ('SSC_CGPA', models.IntegerField()),
                ('SSC_Year', models.IntegerField()),
                ('Classes', models.IntegerField()),
                ('CaseStudies', models.IntegerField()),
                ('MockTests', models.IntegerField()),
                ('Interviews', models.IntegerField()),
                ('Project', models.CharField(max_length=25)),
                ('Feedback', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=25)),
            ],
        ),
    ]
