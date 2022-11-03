from django.urls import path
from .views import loginuser,logoutuser,registration,change_password,activate,UserProfile
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
app_name= 'session'

urlpatterns = [
    path('login/', loginuser,name="login"),
    path('logout/', logoutuser,name="logout"),
    path('userpro/', UserProfile,name="UserProfile"),
    path('ownerprofile/', ownerprofile,name="ownerprofile"),
    path('signup/', registration,name="signup"),
    path('password/', change_password,name="password"),
    path('activate/<uidb64>/<token>/', activate,name="activate"),

    path('reset/password/', PasswordResetView.as_view(template_name='session/reset_password.html'),name="password_reset"),
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='session/reset_pass_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='session/reset_pass_confirm.html'),name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='session/password_reset_complete.html'),name="password_reset_complete"),
]