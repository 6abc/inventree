from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add_item'),
    path('add-location/', views.add_location, name='add_location'),
    # ✅ EDIT
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),
    # ❌ DELETE
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]
