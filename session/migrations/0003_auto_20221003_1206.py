# Generated by Django 3.2.8 on 2022-10-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_alter_userprofile_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='blood_group',
            field=models.CharField(choices=[('AB+', 'AB+'), ('A+', 'A+'), ('A-', 'A-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=50, null=True),
        ),
    ]
