# Generated by Django 3.1.7 on 2021-03-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0014_auto_20210325_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselesson',
            name='lesson_video_file',
            field=models.FileField(blank=True, null=True, upload_to='Courses_Contents', verbose_name='Lesson Video File'),
        ),
    ]
