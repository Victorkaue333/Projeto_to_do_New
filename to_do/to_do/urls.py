from django.contrib import admin
from django.urls import path, include
from to_do import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')),
    path('login/', views.login, name='login'),
  

]
