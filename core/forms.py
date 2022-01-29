"""from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
class SignupForm(forms.Form):
    name=forms.CharField(max_length=15,label="name")
    email=forms.EmailField(label="email")
    def signup(self,request,user):
        user.first_name=self.cleaned_data['name']
        user.email=self.cleaned_data['email']
        user.save()"""
from django.forms import ModelForm
#from .models import profile

'''class ProfileForm(ModelForm):
    class Meta:
        model=profile'''
        
