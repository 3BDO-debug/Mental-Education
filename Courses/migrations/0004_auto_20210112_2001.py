# Generated by Django 3.1.5 on 2021-01-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_auto_20210112_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselesson',
            name='lesson_video_link',
            field=models.CharField(blank=True, max_length=700, null=True, verbose_name='Lesson Video Link'),
        ),
    ]
