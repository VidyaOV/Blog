from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from adminpanel.models import Profile,Comment,Blog_Table


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'id_proof', 'phone_number']
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'id_proof': forms.FileInput(attrs={'class': 'form-control-file'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
               }

   
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add your comment here...'})
                   }


class CommentStatusForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['status']
        widgets = {
            'status': forms.RadioSelect(choices=Comment.STATUS_CHOICES),
        }
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_Table
        fields = ['title', 'content', 'blog_image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'blog_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=Blog_Table.STATUS_CHOICES),
             }
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']



    