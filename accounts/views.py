#Imports Login-Register-Logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from accounts.forms import User_registration_form, Contact_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from accounts.models import Local

#Modulo Login:
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                form = AuthenticationForm()
                return render(request, 'auth/login.html')
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

#Modulo Register:
def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return render(request, 'index.html')
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)

#Logout:
def logout_view(request):
    logout(request)
    return redirect('/')

#Contact Form:
@login_required
def contact_view(request):
    data = {
        'contact_form': Contact_form()
    }
    if request.method == 'POST':
        contact_full = Contact_form(data=request.POST)
        if contact_full.is_valid():
            contact_full.save()
            data["message"] = "Contacto enviado"
        else:
            data['contact_form'] = contact_full
    return render(request, 'contact_form.html', data)

#Create Local Form:
class Create_Local(LoginRequiredMixin, CreateView):
    model = Local
    template_name = 'local_form.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')
