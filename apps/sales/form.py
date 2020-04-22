from django import forms #Se importa los forms de Django

from apps.sales.models import Sale #importar el Modelo

#Se crea la clase
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale #Se incluye el modelo en donde proviene
        fields = [
        	'date',
        	'discount',
        	'subtotal',
        	'total',
            'user',
            'clients',
        ] #Se incluyen los campos de ese modelo

        labels = {
        	'date': 'Fecha',
        	'discount': 'Descuento',
        	'subtotal': 'Subtotal',
        	'total': 'Total',
            'user': 'Usuario',
            'clients': 'Cliente',
        }   	# Son las etiquetas a la hora de trazar el formulario

        widgets = {
        'date':forms.DateInput(attrs={'class':'form-control'}),
        'discount':forms.TextInput(attrs={'class':'form-control'}),
        'subtotal':forms.TextInput(attrs={'class':'form-control'}),
        'total':forms.TextInput(attrs={'class':'form-control'}),
        'user':forms.Select(attrs={'class':'form-control'}),
        'clients':forms.Select(attrs={'class':'form-control'}),
        }   	# Los widgets sirve para definir los campos del formulario