from django.urls import path, include
from apps.products.views import index

urlpatterns = [
    path('', index),
]
