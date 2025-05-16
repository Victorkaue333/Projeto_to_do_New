from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

#lógica para a tela de login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Aqui você pode adicionar lógica para validar o usuário e senha
            return render(request, 'to_do/home.html', {'username': username})
    else:
        form = LoginForm()
    
    return render(request, 'to_do/login.html', {'form': form})

