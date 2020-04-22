from django import forms #Se importa los forms de Django
 
from apps.products.models import Product, ProductType #importar el Modelo
 
#Se crea la clase
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product #Se incluye el modelo en donde proviene
        fields = [
        	'name',
        	'quantity',
        	'price',
        	'description',
            'mark',
            'product_types',
        ] #Se incluyen los campos de ese modelo
 
        labels = {
         	'name': 'Nombre',
        	'quantity': 'Cantidad',
        	'price': 'Precio',
        	'description': 'Descripción',
            'mark': 'Marca',
            'product_types':'Tipo porducto',
        }   	# Son las etiquetas a la hora de trazar el formulario
 
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'quantity':forms.TextInput(attrs={'class':'form-control'}),
        'price':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.TextInput(attrs={'class':'form-control'}),
        'mark':forms.TextInput(attrs={'class':'form-control'}),
        'genders':forms.Select(attrs={'class':'form-control'}),
    	'product_types':forms.Select(attrs={'class':'form-control'}),	
        }   	# Los widgets sirve para definir los campos del formulario


class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType #Se incluye el modelo en donde proviene
        fields = [
        	'name',
        ] #Se incluyen los campos de ese modelo
 
        labels = {
         	'name': 'Nombre',
        }   	# Son las etiquetas a la hora de trazar el formulario
 
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        }
