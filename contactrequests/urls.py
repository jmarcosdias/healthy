"""
Definition of the URLs for the contact requests app
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_contact_requests, name='contact_requests'),
    path('add/', views.add_contact_request, name='add_contact_request'),
    path('edit/<int:contact_request_id>/', views.edit_contact_request, name='edit_contact_request'),
    path('delete/<int:contact_request_id>/', views.delete_contact_request, name='delete_contact_request'),
    path('confirm_delete/<int:contact_request_id>/', views.confirm_delete_contact_request, 
         name='confirm_delete_contact_request'),
]