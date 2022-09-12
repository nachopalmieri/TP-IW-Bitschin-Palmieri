from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class FormRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormInicioSesion(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
