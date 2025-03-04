from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    class Meta: 
        model = User 
        fields = {'username', 'email'}