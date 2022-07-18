from django.views.generic import ListView
from django.shortcuts import render
from accounts.models import Local

#Inicio:
def index(request):
    return render(request, 'index.html')

#Ver Locales:
class Mostrar_Locales(ListView):
    model = Local
    template_name = 'all.html'
    queryset = Local.objects.all()