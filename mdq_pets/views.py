from django.shortcuts import render

#Inicio:
def index(request):
    return render(request, 'index.html')

