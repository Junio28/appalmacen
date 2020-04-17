from django.shortcuts import render, redirect

from django.views.generic import CreateView
# Create your views here.
from apps.products.models import Product  #Se le incluye el modelo
from apps.products.form import ProductForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'products/index.html')

 #Definir la vista del formulario
class ProductCreate(CreateView):
   model = Product
   form_class = ProductForm
   template_name = 'products/product_form.html'
   success_url = reverse_lazy('producto:product') 


