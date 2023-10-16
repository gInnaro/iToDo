from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Note


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class Loginform(forms.Form):
    username = forms.CharField(max_length= 25, label="Enter username")
    password = forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', )
        widgets = {
            'authors': forms.HiddenInput(),
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название категории"})
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'description')
        widgets = {
            'authors': forms.HiddenInput(),
            'title': forms.TextInput(attrs={
                'class': "input_note_title",
                'placeholder': "Название заметки"}),
            'description': forms.Textarea(attrs={
                'class': "input_note_description",
                'placeholder': "Содержимое заметки"}),
            'category_id': forms.Select(attrs={
                'class': "input_note_category",
                'placeholder': "Категория"}),
        }