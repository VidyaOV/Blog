from django.urls import path
from . import views

urlpatterns = [
  
   path('', views.home,name='home'),
   path('login/', views.user_login,name='userlogin'),
   path('otp/', views.otp,name='otp'),
   path('registration/', views.registration, name='registration'),
   path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
   path('resetpassword/', views.resetpassword, name='resetpassword'),
   path('userlogout/', views.userlogout, name='userlogout'),
   path('about/', views.about, name='about'),
]