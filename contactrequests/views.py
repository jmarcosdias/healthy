"""
Contact requests views here
"""


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactRequest
from .forms import ContactRequestForm, AddContactRequestForm


@login_required
def all_contact_requests(request):
    """ A view to show all contact_requests """

    contact_requests = ContactRequest.objects.filter(created_by=request.user)

    context = {
        'contact_requests': contact_requests
    }

    return render(request, 'contact_requests/contact_requests.html', context)


@login_required
def edit_contact_request(request, contact_request_id):
    """ Edit a contact request """
    contact_request = get_object_or_404(ContactRequest, pk=contact_request_id)
    if not request.user == contact_request.created_by:
        messages.error(request, 'Sorry, you can only edit contact requests you have \
                       written!')
        return redirect(reverse('contact_requests'))

    if request.method == 'POST':
        form = ContactRequestForm(request.POST, request.FILES, instance=contact_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated contact request!')
            return redirect(reverse('contact_requests'))
        else:
            messages.error(request, 'Failed to update contact request. Please ensure \
                                     the form is valid!')
    else:
        form = ContactRequestForm(instance=contact_request)
        messages.info(request, f'You are editing a contact request!')

    template = 'contact_requests/edit_contact_request.html'
    context = {
        'form': form,
        'contact_request': contact_request,
    }

    return render(request, template, context)


@login_required
def confirm_delete_contact_request(request, contact_request_id):
    """ Confirm deletion of a contact request """
    contact_request = get_object_or_404(ContactRequest, pk=contact_request_id)
    if not request.user == contact_request.created_by:
        messages.error(request, 'Sorry, you can only delete contact requests you have \
                       written!')
        return redirect(reverse('contact_requests'))
    
    template = 'contact_requests/confirm_delete_contact_request.html'
    context = {
        'contact_request': contact_request,
    }

    return render(request, template, context)


@login_required
def delete_contact_request(request, contact_request_id):
    """ Delete a contact request """
    contact_request = get_object_or_404(ContactRequest, pk=contact_request_id)
    if not request.user == contact_request.created_by:
        messages.error(request, 'Sorry, you can only delete contact requests you have \
                       written!')
        return redirect(reverse('contact_requests'))
    contact_request.delete()
    messages.success(request, 'Contact request deleted!')
    return redirect(reverse('contact_requests'))


@login_required
def add_contact_request(request):
    """ Add a contact_request """
    if request.method == 'POST':
        form = AddContactRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added contact request!')
            return redirect(reverse('contact_requests'))
        else:
            messages.error(request, 'Failed to add contact request. Please ensure the \
                           form is valid!')
    else:
        form = AddContactRequestForm(initial={
            'created_by': request.user,
        })

    template = 'contact_requests/add_contact_request.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
