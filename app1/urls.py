from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add_item'),
    path('add-location/', views.add_location, name='add_location'),
]