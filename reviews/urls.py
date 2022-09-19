"""
Definition of the URLs for the reviews app
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews'),
    path('add/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('confirm_delete/<int:review_id>/', views.confirm_delete_review, 
         name='confirm_delete_review'),
]