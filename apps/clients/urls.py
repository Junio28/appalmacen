from django.urls import path, include
from  apps.clients.views import index, ClientCreate, ClientList, ClientUpdate

app_name = 'cliente'

urlpatterns = [
    path('', index, name='client'),
    path('nuevo/', ClientCreate.as_view(), name='client_new'),
    path('listar/', ClientList.as_view(), name='client_list'),
    path('editar/<int:pk>/', ClientUpdate.as_view(),name='client_edit'),
]