from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"to_do/home.html")

def main_view(request):
    return render(request, 'templates_to_do/main.html')