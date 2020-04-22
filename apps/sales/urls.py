from django.urls import path, include
from apps.sales.views import index

urlpatterns = [
    path('', index),
]