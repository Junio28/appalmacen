from django.shortcuts import render, redirect
from django.views.generic import CreateView
# Create your views here.
from apps.sales.models import Sale  #Se le incluye el modelo
from apps.sales.form import SaleForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'sales/index.html')

class SaleCreate(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sales/sale_form.html'
    success_url = reverse_lazy('venta:sale') 
