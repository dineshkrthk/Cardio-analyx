# Generated by Django 4.1.3 on 2022-11-24 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_patientprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='lastname',
        ),
    ]
