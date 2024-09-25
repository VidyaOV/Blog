from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Profile,Blog_Table,Comment
from django.contrib.auth.models import User
from userpanel.forms import CommentStatusForm,LoginForm
from adminpanel.models import Blog_Table,Comment,Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm




# Create your views here.
def adminlogin(request):
   if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user = authenticate(request, username=username, password=password)
          if user is not None and user.is_superuser:
             login(request, user)
             messages.success(request, "You have successfully logged in.")
             return redirect('adminhome')  
          else:
            messages.error(request, "Invalid username or password.")
            print("ERROR")
            return redirect('adminlogin')
   else:
      form = LoginForm()
   return render(request, 'adminpanel/adminlogin.html', {'form': form})



def adminhome(request):
    return render(request,'adminpanel/admin_home.html')

def bloglist(request):
  blogs = Blog_Table.objects.all().order_by("-created_at")
  return render(request, 'adminpanel/blog_list.html', {'blogs': blogs})
 


def blogview(request,pk):
  blog = Blog_Table.objects.get(id=pk)
  comments = Comment.objects.filter(blog_id=blog)
  if request.method == 'POST':
     comment_id = request.POST.get('comment_id')
     comment = get_object_or_404(Comment, id=comment_id)
     form = CommentStatusForm(request.POST, instance=comment)
     if form.is_valid():
       comment.save()
       messages.success(request, "Admin changed the comment status")
       return redirect('blogview', pk = blog.id)
     else:
        messages.error(request, 'There was an error with your submission. Please check for the errors.') 
  else:
      form = CommentStatusForm()

  return render(request,'adminpanel/blog_view.html',{'blog':blog,'comments':comments,'form':form})

 
def adminresetpassword(request):
    return render(request,'adminpanel/reset_password.html')


def userlist(request): 
  profiles = Profile.objects.select_related('user')
  return render(request, 'adminpanel/user_list.html', {'profiles': profiles})


def viewuser(request, pk):
    user = get_object_or_404(User, id=pk)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'adminpanel/view_user.html', {'user': user, 'profile': profile})


def adminlogout(request):
   logout(request)
   messages.success(request, "You have successfully logged out.")
   return redirect('adminlogin')


@staff_member_required
def adminresetpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Admins password is successfully updated!')
            return redirect('adminhome')  # Redirect to the admin index page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'adminpanel/reset_password.html', {'form': form})