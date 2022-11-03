from distutils.command.upload import upload
import email
from email.mime import image
from email.policy import default
from sre_constants import CATEGORY
from turtle import title
from unicodedata import category, name
from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from sqlalchemy import true

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    content=models.TextField()
    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Class_in(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY={
        ('Teacher','Teacher'),
        ('Student','Student'),
    }
    MEDIUM=(
        ('bangla','bangla'),
        ('English','English'),
        ('Math','Math'),
        ('Hindi','Hindi'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null= True)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=101)
    slug=models.CharField(max_length=100, default=title)
    email=models.EmailField()
    salary=models.FloatField()
    details=models.TextField()
    available=models.BooleanField()
    category=models.CharField(max_length=100,choices=CATEGORY)
    created_at=models.DateTimeField(default=now)
    image=models.ImageField(default='default.jpg',upload_to='tution/images')
    medium=MultiSelectField(max_length=100, max_choices=5,choices=MEDIUM,default='bangla')
    Subject=models.ManyToManyField(Subject,related_name='subject_name')
    Class_in=models.ManyToManyField(Class_in,related_name='class_set')
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)