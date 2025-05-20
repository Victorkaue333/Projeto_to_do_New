from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Tela de Home
def home(request):
    return render(request, "to_do/home.html" )

#  Tela de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    
    return render(request, 'to_do/login.html', {'form': form})

# Tela de Cadastro
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    
    return render(request, 'to_do/cadastro.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Tela principal
def main_view(request):
    return render(request, 'tarefas/main.html')
