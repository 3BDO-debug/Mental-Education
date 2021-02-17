# Generated by Django 3.1.6 on 2021-02-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_View', '0003_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_pic', models.ImageField(upload_to='Best_Students_Photos', verbose_name='Student Pic')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Best Student',
                'verbose_name_plural': 'Best Students',
            },
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_member_pic', models.ImageField(upload_to='Staff_Members_Photos', verbose_name='Staff Member Picture')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Staff Member',
                'verbose_name_plural': 'Staff Members',
            },
        ),
    ]
