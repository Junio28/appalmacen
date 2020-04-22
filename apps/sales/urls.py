from django.urls import path, include
from apps.sales.views import index, SaleCreate

app_name = 'venta'

urlpatterns = [
    path('', index, name='sale'),
    path('nuevo/', SaleCreate.as_view(), name='sale_new'),
]