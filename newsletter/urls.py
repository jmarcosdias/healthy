"""
Definition of the URLs for the newsletter app
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe_newsletter, name='subscribe_newsletter'),
    # path('', views.unsubscribe_newsletter, name='unsubscribe_newsletter'),
]