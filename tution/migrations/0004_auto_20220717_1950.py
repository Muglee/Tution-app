# Generated by Django 3.2.8 on 2022-07-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0003_auto_20220716_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='tution/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100),
        ),
    ]
