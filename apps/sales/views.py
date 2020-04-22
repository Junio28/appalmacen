from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
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
    success_url = reverse_lazy('venta:sale_list') 

class SaleList(ListView):
       model = Sale
       template_name = 'sales/sale_list.html'

class SaleUpdate(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sales/sale_form.html'
    success_url = reverse_lazy('venta:sale_list')

