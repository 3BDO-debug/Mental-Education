# Generated by Django 3.1.5 on 2021-01-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
        ('Courses', '0010_course_created_at'),
        ('Accounts', '0007_user_user_on_going_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_on_going_courses',
        ),
        migrations.AddField(
            model_name='user',
            name='user_selected_courses',
            field=models.ManyToManyField(blank=True, to='Courses.Course', verbose_name="User's on going courses"),
        ),
        migrations.AlterField(
            model_name='user',
            name='selected_subjects',
            field=models.ManyToManyField(blank=True, null=True, to='Subjects.Subject', verbose_name="Users' Selected Subjects"),
        ),
    ]
