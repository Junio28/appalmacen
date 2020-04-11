from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

# Create your views here.
from apps.clients.models import Client  #Se le incluye el modelo
from apps.clients.form import ClientForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'clients/index.html')

#Definir la vista del formulario
class ClientCreate(CreateView):
   model = Client
   form_class = ClientForm
   template_name = 'clients/client_form.html'
   success_url = reverse_lazy('cliente:client_list') 

class ClientList(ListView):
    model = Client
    template_name = 'clients/client_list.html'




