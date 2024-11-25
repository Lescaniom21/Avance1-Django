from django.urls import path
from . import views

urlpatterns = [
path('', views.Productos, name='Productos'),
path('Vista1/', views.Vista1, name='Vista1'),
]
