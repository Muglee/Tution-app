from audioop import ulaw2lin
from email import message
import email
import imp
from typing import Type
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import ownerprofile, authenticate,login,logout,update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
Usermodel=get_user_model()

# Create your views here.
def loginuser(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homeview')
            else:
                messages.error(request,'Invalid Username or password')
        else:
                messages.error(request,'Invalid Username or password')
    else:
        form=AuthenticationForm()
    return render(request,'session/login.html',{'form':form})
def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully logout')
    return redirect('homeview')
from .forms import SignUpForm
def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            mail_subject='Activate your account'
            message=render_to_string('session/account.html',{
                'user':user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            send_mail=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message, to=[send_mail])
            email.send()
            message.success(request,'succesfully created account')
            message.success(request,'Password has successfully changed')
            return redirect('login')
    else:
        form=SignUpForm
    return render(request,'session/signup.html',{'form':form})
def activate(request, uidb64, token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Usermodel._default_manager.get(pk=uid)    
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user=token):
        user.is_active=True
        user.save()
        messages.success(request,"Your account is activate")
        return redirect('login')
    else:
        messages.warning(request,"activation link is valid")
        return redirect('signup')
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        update_session_auth_hash(request,form.user)
        messages.success(request,"Password has changed")
        return redirect('homeview')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'session/change.html',{'form':form})

from .forms import UserProfileForm   
def UserProfile(request):
    try:
        instance= UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExit:
        instance=None
    if request.method=="POST":
        if instance:
            form=UserProfileForm(request.POST,request.FILES,instance=instance)
        else:
            form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            message.success(request,"success") 
    else:
        form=UserProfileForm(instance=instance)
    context={
        'form':form
    }
    return render(request,'session/userproCreate.html',context)

def ownerprofile(request):
    user=request.user
    return render (request,'session/userprofile.html',{'user':user})


    