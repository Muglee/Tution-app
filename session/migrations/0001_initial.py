# Generated by Django 3.2.8 on 2022-09-27 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('blood_group', models.CharField(choices=[('AB+', 'AB+'), ('A-', 'A-'), ('A+', 'A+')], max_length=3)),
                ('gender', models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE')], max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('nationality', models.CharField(max_length=30)),
                ('religion', models.CharField(max_length=50)),
                ('biodata', models.TextField()),
                ('profession', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=50, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='session/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
