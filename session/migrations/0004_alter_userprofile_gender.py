# Generated by Django 3.2.8 on 2022-10-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20221003_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE')], max_length=50),
        ),
    ]
