from pyexpat import model
from tkinter import Widget
from unittest import mock
from django import forms
from .models import Contact,Post

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
class ContactFormtwo(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','id','created_at','slug']
        Widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
                }),
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
                })
        }
        