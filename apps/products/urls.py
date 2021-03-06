from django.urls import path, include
from apps.products.views import index, ProductCreate, ProductList, ProductUpdate, ProductDelete, ProductTypeCreate, ProductTypeList, ProductTypeUpdate, ProductTypeDelete

app_name='producto'

urlpatterns = [
    path('', index, name='product'),
    path('nuevo/', ProductCreate.as_view(), name='product_new'),
    path('listar/', ProductList.as_view(), name='product_list'),
    path('editar/<int:pk>/', ProductUpdate.as_view(),name='product_edit'),
    path('eliminar/<int:pk>/', ProductDelete.as_view(),name='product_delete'),
    path('tipo_producto/nuevo/', ProductTypeCreate.as_view(), name='productType_new'),
    path('tipo_producto/listar/', ProductTypeList.as_view(), name='productType_list'),
    path('tipo_producto/editar/<int:pk>/', ProductTypeUpdate.as_view(),name='productType_edit'),
    path('tipo_producto/eliminar/<int:pk>/', ProductTypeDelete.as_view(),name='productType_delete'),
]
