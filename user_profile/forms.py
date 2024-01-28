from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

class ProfileTgKey(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tg_id', 'tg_key']
        widgets = {
            'tg_id': forms.HiddenInput(),
            'tg_key': forms.HiddenInput(),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
