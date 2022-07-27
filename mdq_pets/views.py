from django.views.generic import ListView, DetailView
from django.shortcuts import render
from accounts.models import Local

#Inicio:
def index(request):
    inicio = Local.objects.all()[:3]
    return render(request, 'index.html', {'inicio': inicio})

#Ver Locales:
class Mostrar_Locales(ListView):
    model = Local
    template_name = 'all.html'
    queryset = Local.objects.all()

#Detalles Local:
class Ver_Local(DetailView):
    model = Local
    template_name = 'local.html'