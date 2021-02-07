# Generated by Django 3.1.5 on 2021-01-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
        ('Accounts', '0003_auto_20210112_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='selected_subjects',
            field=models.ManyToManyField(to='Subjects.Subject', verbose_name="Users' Selected Subjects"),
        ),
    ]