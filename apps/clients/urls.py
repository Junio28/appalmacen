from django.urls import path, include
from  apps.clients.views import index, ClientCreate, ClientList

app_name = 'cliente'

urlpatterns = [
    path('', index, name='client'),
    path('nuevo/', ClientCreate.as_view(), name='client_new'),
    path('listar/', ClientList.as_view(), name='client_list'),
]