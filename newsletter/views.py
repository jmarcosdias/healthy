"""
Views for the newsletter app
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import NewsletterSubscription
from .forms import NewsletterForm


def subscribe(request):
    """ A view to handle newsletter subscription """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter_subscription = form.save()
            messages.success(request, 'Thank you for subscribing to \
                 our newsletter!')
            return redirect(reverse('home'))
    
    messages.error(request, 'Sorry, we were unable to fulfill your reqest. \
        Please review your input!')

    context = {
        'form': form,
    }

    return render(request, 'newsletter/subscribe_newsletter.html', context)


def unsubscribe(request):
    """ A view to handle newsletter unsubscription """
    form = NewsletterForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        return redirect(reverse('unsubscribe_newsletter_email', args=[email]))

    context = {
        'form': form,
    }

    return render(request, 'newsletter/unsubscribe_newsletter.html', context)


def unsubscribe_email(request, email):
    """ A view to unsubscribe a specific email """
    try:
        newsletter_subscription = get_object_or_404(NewsletterSubscription,
                                                    email=email)
        newsletter_subscription.delete()
        messages.success(request, f'We have unsubscribed {newsletter_subscription.email} \
            from our newsletter!')
        return redirect(reverse('home'))

    except Http404:       
        messages.error(request, f'Sorry, we are not finding this email. \
            Are you sure you subscribed {email} before?')

        return redirect(reverse('unsubscribe_newsletter'))
