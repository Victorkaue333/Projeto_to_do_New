# to_do/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# --- ESTE É O FORMULÁRIO QUE ESTAVA FALTANDO ---
class LoginForm(AuthenticationForm):
    # O AuthenticationForm já vem com os campos de usuário e senha.
    # Podemos estilizá-los aqui se quisermos, mas por enquanto, isso é o suficiente.
    pass


# --- ESTE É O FORMULÁRIO DE CADASTRO QUE JÁ FIZEMOS ---
class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Obrigatório. Um endereço de e-mail válido.'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')