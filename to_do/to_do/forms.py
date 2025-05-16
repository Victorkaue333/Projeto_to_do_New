# accounts/forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class CadastroForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)