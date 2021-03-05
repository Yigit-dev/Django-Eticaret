from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image


class SearchForm(forms.Form):
  query = forms.CharField(label='Search', max_length = 100)

class SignUpForm(UserCreationForm):
  username = forms.CharField(max_length=30, label= 'User Name: ')
  email = forms.EmailField(max_length=200, label= 'Email : ')
  first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name :')
  last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name :')
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image', 'title']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
        }

class ImageEditForm(forms.Form):
    thresh = forms.IntegerField(label='filtrele', min_value=0, max_value=255)