from django.urls import path, include
from  apps.clients.views import index, ClientCreate, ClientList, ClientUpdate, ClientDelete

app_name = 'cliente'

urlpatterns = [
    path('', index, name='client'),
    path('nuevo/', ClientCreate.as_view(), name='client_new'),
    path('listar/', ClientList.as_view(), name='client_list'),
    path('editar/<int:pk>/', ClientUpdate.as_view(),name='client_edit'),
    path('eliminar/<int:pk>/', ClientDelete.as_view(),name='client_delete'),
]