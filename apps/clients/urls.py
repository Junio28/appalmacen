from django.urls import path, include
from  apps.clients.views import index

urlpatterns = [
    path('', index),
]