from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.
from apps.products.models import Product, ProductType #Se le incluye el modelo
from apps.products.form import ProductForm, ProductTypeForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'products/index.html')

#Definir la vista del formulario
class ProductCreate(CreateView):
   model = Product
   form_class = ProductForm
   template_name = 'products/product_form.html'
   success_url = reverse_lazy('producto:product_list') 


class ProductList(ListView):
       model = Product
       template_name = 'products/product_list.html'

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/Product_form.html'
    success_url = reverse_lazy('producto:product_list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('producto:product_list')


class ProductTypeCreate(CreateView): 
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'products/productType/productType_form.html'
    success_url = reverse_lazy('producto:productType_list')

class ProductTypeList(ListView):
       model = ProductType
       template_name = 'products/productType/productType_list.html'

class ProductTypeUpdate(UpdateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'products/productType/productType_form.html'
    success_url = reverse_lazy('producto:productType_list')


class ProductTypeDelete(DeleteView):
    model = ProductType
    template_name = 'products/productType/productType_delete.html'
    success_url = reverse_lazy('producto:productType_list')




