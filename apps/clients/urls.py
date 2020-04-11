from django.urls import path, include
from  apps.clients.views import index, ClientCreate

app_name = 'cliente'

urlpatterns = [
    path('', index, name='client'),
    path('nuevo/', ClientCreate.as_view(), name='client_new'),
]