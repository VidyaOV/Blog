from django.shortcuts import render,redirect
from django.http import HttpResponse
from userpanel.forms import RegistrationForm,ProfileForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from adminpanel.models import Blog_Table

# Create your views here.
def home(request):
  blogs = Blog_Table.objects.filter(status='published').order_by("-created_at") 
  return render(request,'sitevisitor/home.html',{'blogs': blogs})
  

def otp(request):
    return render(request,'sitevisitor/otp.html')

def forgotpassword(request):
    return render(request,'sitevisitor/forgot_password.html')

def resetpassword(request):
    return render(request,'sitevisitor/reset_password.html')


def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Registration successful! You can now login.")
            return redirect('userlogin')
    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'sitevisitor/registration.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
  if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           messages.success(request, "You have successfully logged in.")
           return redirect('userhome')  
        else:
            messages.error(request, "Invalid username or password.")
            print("ERROR")
            return redirect('userlogin')
  else:
      form = LoginForm()
    
  return render(request, 'sitevisitor/login.html', {'form': form})




def userlogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

def about(request):
    return render(request,'sitevisitor/about.html')

