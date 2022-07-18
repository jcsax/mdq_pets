from django.urls import path
from accounts.views import login_view, logout_view, register_view, \
Profile_view, Update_profile, \
contact_view

urlpatterns = [
    path('iniciar-sesion/', login_view, name = 'login'),
    path('cerrar-sesion/', logout_view, name = 'logout'),
    path('registrarse/', register_view, name = 'register'),
    path('contacto/', contact_view, name = 'contact_form'),
    path('perfil/', Profile_view, name = 'profile'),
    path('perfil/actualizar/<int:pk>/', Update_profile.as_view(), name = 'profile_update')
    
]