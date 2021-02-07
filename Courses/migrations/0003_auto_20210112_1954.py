# Generated by Django 3.1.5 on 2021-01-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20210112_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(default='Course Description Goes here.', verbose_name='Course Description'),
        ),
        migrations.AddField(
            model_name='course',
            name='tutored_by',
            field=models.CharField(default="Course's Tutor Name Goes Here.", max_length=350, verbose_name='Tutored By'),
        ),
    ]