from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blogview/<int:pk>/', views.blogview, name='blogview'),
    path('adminresetpassword/', views.adminresetpassword, name='adminresetpassword'),
    path('userlist/', views.userlist, name='userlist'),
    path('viewuser/<int:pk>/', views.viewuser, name='viewuser'),
    # path('editcomment/<int:pk>/', views.editcomment, name='editcomment'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
   
    # path('accounts/',include("django.contrib.auth.urls"))
    # path('adminpanel/accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset')
   

   
]