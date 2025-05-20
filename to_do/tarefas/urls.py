from django.urls import path
from .views import home, main_view  # Importa as duas views corretamente

urlpatterns = [
    
    path('', home, name='home'),            # Rota raiz
    path('main/', main_view, name='main'),  # Rota para /main/
]
