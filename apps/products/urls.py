from django.urls import path, include
from apps.products.views import index, ProductCreate, ProductList, ProductUpdate

app_name='producto'

urlpatterns = [
    path('', index, name='product'),
    path('nuevo/', ProductCreate.as_view(), name='product_new'),
    path('listar/', ProductList.as_view(), name='product_list'),
    path('editar/<int:pk>/', ProductUpdate.as_view(),name='product_edit'),
]
