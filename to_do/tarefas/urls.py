from .views import home
from django.urls import path, include
from .views import main_view

urlpatterns = [
    path('', home, name='home'),
    path('', include('to_do.urls')),
    path('', main_view, name='main'),
]
