from django.urls import path
from accounts.views import login_view, logout_view, register_view, \
contact_view, Create_Local

urlpatterns = [
    path('iniciar-sesion/', login_view, name = 'login'),
    path('cerrar-sesion/', logout_view, name = 'logout'),
    path('registrarse/', register_view, name = 'register'),
    path('contacto/', contact_view, name = 'contact_form'),
    path('registrar-local/', Create_Local.as_view(), name = 'local_form'),
    
]