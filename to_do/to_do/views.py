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
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # Cria novo usuário
            login(request, user)    # Faz login automático após cadastro
            return redirect('home')  # Pode ser 'home' ou outra tela
    else:
        form = UserCreationForm()
    
    return render(request, 'to_do/cadastro.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
