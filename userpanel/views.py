from django.shortcuts import render,redirect,get_object_or_404
from .forms import BlogForm,CommentForm,ProfileForm,RegistrationForm
from adminpanel.models import Blog_Table,Comment,Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def userhome(request):
   return render(request,'userpanel/user_home.html')

def fullbloglist(request):
   blogs = Blog_Table.objects.all().order_by("-created_at")
   return render(request, 'userpanel/blog_list.html', {'blogs': blogs})

def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  
            blog.save()
            messages.success(request, 'Your blog post has been added successfully.')
            return redirect('fullbloglist') 
        else:
            messages.error(request, 'There was an error with your submission. Please check for the errors.') 
    else:
        form = BlogForm()
    
    return render(request, 'userpanel/add_blog.html', {'form': form})

def addcomment(request,pk):
    blog = Blog_Table.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('viewblog', pk= blog.id)
        else:
            messages.error(request, 'There was an error with your submission. Please check for the errors.') 
    else:
        form = CommentForm()

    return render(request, 'userpanel/add_comment.html', {'form': form, 'blog': blog})
   
    
def viewblog(request,pk):
    blog = Blog_Table.objects.get(id=pk)
    comments = Comment.objects.filter(blog_id=blog, status='view')
    return render(request,'userpanel/view_blog.html',{'blog':blog,'comments':comments})
    
  
def editblog(request,pk):
   blog = Blog_Table.objects.get(id=pk)
   form = BlogForm(request.POST, request.FILES,instance=blog)
   if request.method == 'POST':
       form = BlogForm(request.POST, request.FILES, instance=blog)
       if form.is_valid():
            form.save()
            messages.success(request, 'Your blog post has been updated successfully.')
            return redirect('fullbloglist')
       else:
            messages.error(request, 'There was an error .')
   else:
        form = BlogForm(instance=blog)
   return render(request, 'userpanel/edit_blog.html', {'form': form, 'blog': blog})


def deleteblog(request,pk):
   blog = Blog_Table.objects.get(id=pk)
   blog.delete()
   messages.success(request, 'Blog post deleted successfully.')
   return redirect('fullbloglist')

def deletecomment(request,pk):
   comment = Comment.objects.get(id=pk)
   blog_id = comment.blog_id.id
   comment.delete()
   messages.success(request, 'Your comment deleted successfully.')
   return redirect('viewblog',pk=blog_id)


def myblogs(request):
    user = request.user
    blogs = Blog_Table.objects.filter(author=user)
    return render(request, 'userpanel/my_blogs.html', {'blogs': blogs})
   
def viewprofile(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  return render(request, 'userpanel/view_profile.html', {'profile': profile})
   

def editprofile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
         form = ProfileForm(request.POST, request.FILES, instance=profile)
         if form.is_valid():
             form.save()
             messages.success(request, 'Your profile has been updated successfully.')
             return redirect('viewprofile')
         else:
            messages.error(request, 'There was an error .')
    else: 
         form = ProfileForm(instance=profile)
    return render(request, 'userpanel/edit_profile.html', {'form': form})


@login_required
def userresetpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('viewprofile')  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'userpanel/reset_password.html', {'form': form})

   

