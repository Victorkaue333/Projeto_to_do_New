from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import LoginForm  # Se você quiser usar seu próprio LoginForm futuramente

# Tela de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Obtém o usuário autenticado
            login(request, user)    # Faz login
            return redirect('home')  # Redireciona para a tela principal
    else:
        form = AuthenticationForm()
    
    return render(request, 'to_do/login.html', {'form': form})

# Tela de Cadastro
from .forms import CadastroForm # Importe o formulário
from django.contrib import messages

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Faça o login.')
            return redirect('login') # Redireciona para a página de login
    else:
        form = CadastroForm()
    
    return render(request, 'to_do/cadastro.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
