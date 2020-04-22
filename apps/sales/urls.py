from django.urls import path, include
from apps.sales.views import index, SaleCreate, SaleList, SaleUpdate, SaleDelete

app_name = 'venta'

urlpatterns = [
    path('', index, name='sale'),
    path('nuevo/', SaleCreate.as_view(), name='sale_new'),
    path('listar/', SaleList.as_view(), name='sale_list'),
    path('editar/<int:pk>/', SaleUpdate.as_view(),name='sale_edit'),
    path('eliminar/<int:pk>/', SaleDelete.as_view(),name='sale_delete'),
]