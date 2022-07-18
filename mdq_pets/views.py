from django.views.generic import ListView
from django.shortcuts import render
from accounts.models import Profile

#Inicio:
def index(request):
    return render(request, 'index.html')

#Ver Perfiles:
class All_profiles(ListView):
    model = Profile
    template_name = 'all.html'
    queryset = Profile.objects.all()