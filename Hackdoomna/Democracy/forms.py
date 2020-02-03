from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel, Vote
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = {'username', 'password1', 'password2'}


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = "__all__"
