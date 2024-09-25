from django.urls import path
from . import views

urlpatterns = [
   path('userhome/', views.userhome, name='userhome'),
   path('fullbloglist/', views.fullbloglist, name='fullbloglist'),
   path('addblog/', views.addblog, name='addblog'),
   path('viewblog/<int:pk>/', views.viewblog, name='viewblog'),
   path('editblog/<int:pk>/', views.editblog, name='editblog'),
   path('deleteblog/<int:pk>/', views.deleteblog, name='deleteblog'),
   path('deletecomment/<int:pk>/', views.deletecomment, name='deletecomment'),
   path('myblogs/', views.myblogs, name='myblogs'),
   path('viewprofile/', views.viewprofile, name='viewprofile'),
   path('editprofile/', views.editprofile, name='editprofile'),
   path('resetpassword/', views.userresetpassword, name='userresetpassword'),
   path('addcomment/<int:pk>/', views.addcomment, name='addcomment'),
   
   
]