"""
Definition of the URLs for the newsletter app
"""


from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe_newsletter'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe_newsletter'),
    path('unsubscribe/<email>', views.unsubscribe_email,
         name='unsubscribe_newsletter_email'),
]
