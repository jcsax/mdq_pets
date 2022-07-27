from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Contact, Local


#Creación de usuario:
class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

#Formulario de Contacto:
class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

#Formulario para crear local:
class Create_Local_Form(forms.ModelForm):
    class Meta:
        model = Local
        fields = '__all__'