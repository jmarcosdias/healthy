"""
Definition of the URLs for the product requests app
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_product_requests, name='product_requests'),
    path('add/', views.add_product_request, name='add_product_request'),
    path('edit/<int:product_request_id>/', views.edit_product_request, name='edit_product_request'),
    path('delete/<int:product_request_id>/', views.delete_product_request, name='delete_product_request'),
    path('confirm_delete/<int:product_request_id>/', views.confirm_delete_product_request, 
         name='confirm_delete_product_request'),
]