"""
Views for the newsletter app
"""

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import NewsletterSubscription
from .forms import NewsletterForm


def subscribe_newsletter(request):
    """ A view to handle newsletter subscription """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter_subscription = form.save()
            messages.success(request, 'Thank you for subscribing to \
                 our newsletter!')
            return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'newsletter/subscribe_newsletter.html', context)

