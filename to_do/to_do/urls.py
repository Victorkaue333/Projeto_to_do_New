from django.contrib import admin
from django.urls import path, include
from to_do import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main_view, name='main'),
]
