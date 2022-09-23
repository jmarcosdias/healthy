"""
Views for the home app
"""

from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def error_404_view(request, exception):
    """ A view to render the http 404 response page """
    return render(request, 'http_404.html')
