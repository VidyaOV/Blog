from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

#Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_image= models.ImageField(upload_to='profileimages/',blank=True)
  id_proof = models.ImageField(upload_to='idimages/',blank=True)
  phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

  def __str__(self):
    return self.user.username
  

class Blog_Table(models.Model):
  STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
         ]
  title = models.CharField(max_length=250)
  content = models.TextField()
  blog_image = models.ImageField(upload_to='images/',blank=True)
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices= STATUS_CHOICES)

  def __str__(self):
    return self.title
  



class Comment(models.Model):
 
 STATUS_CHOICES = [
        ('view', 'view'),
        ('hidden', 'hidden'),
         ]
 comment = models.TextField()
 author = models.ForeignKey(User,on_delete=models.CASCADE) 
 blog_id= models.ForeignKey(Blog_Table,on_delete=models.CASCADE)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='view')

 def __str__(self):
     return f"{self.blog_id.title} - Comment ID: {self.id}"



