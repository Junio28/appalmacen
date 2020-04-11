from django import forms #Se importa los forms de Django
 
from apps.clients.models import Client #importar el Modelo
 
#Se crea la clase
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client #Se incluye el modelo en donde proviene
        fields = [
        	'name',
        	'lastname',
        	'rut',
        	'address',
            'phone',
        ] #Se incluyen los campos de ese modelo
 
        labels = {
        'name': 'Nombre',       	#Son los nombre que va en la pantalla del formulario
    	'lastname': 'Apellido',       	
    	'rut': 'Identificación',
    	'address': 'Dirección',
        'phone': 'Telefono',
        }   	# Son las etiquetas a la hora de trazar el formulario
 
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
    	'lastname':forms.TextInput(attrs={'class':'form-control'}),
        'rut':forms.TextInput(attrs={'class':'form-control'}),
    	'address':forms.TextInput(attrs={'class':'form-control'}),   	
        'phone':forms.TextInput(attrs={'class':'form-control'}),  
        }   	# Los widgets sirve para definir los campos del formulario
