# Generated by Django 3.1.6 on 2021-02-07 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_user_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='selected_subjects',
        ),
    ]
