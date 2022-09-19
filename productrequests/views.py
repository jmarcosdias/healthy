"""
Product requests views here
"""


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProductRequest
from .forms import ProductRequestForm, AddProductRequestForm


@login_required
def all_product_requests(request):
    """ A view to show all product_requests """

    product_requests = ProductRequest.objects.filter(created_by=request.user)

    context = {
        'product_requests': product_requests
    }

    return render(request, 'product_requests/product_requests.html', context)


@login_required
def edit_product_request(request, product_request_id):
    """ Edit a product request """
    product_request = get_object_or_404(ProductRequest, pk=product_request_id)
    if not request.user == product_request.created_by:
        messages.error(request, 'Sorry, you can only edit product requests you have \
                       written!')
        return redirect(reverse('product_requests'))

    if request.method == 'POST':
        form = ProductRequestForm(request.POST, request.FILES, instance=product_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product request!')
            return redirect(reverse('product_requests'))
        else:
            messages.error(request, 'Failed to update product request. Please ensure \
                                     the form is valid!')
    else:
        form = ProductRequestForm(instance=product_request)
        messages.info(request, f'You are editing a product request!')

    template = 'product_requests/edit_product_request.html'
    context = {
        'form': form,
        'product_request': product_request,
    }

    return render(request, template, context)


@login_required
def confirm_delete_product_request(request, product_request_id):
    """ Confirm deletion of a product request """
    product_request = get_object_or_404(ProductRequest, pk=product_request_id)
    if not request.user == product_request.created_by:
        messages.error(request, 'Sorry, you can only delete product requests you have \
                       written!')
        return redirect(reverse('product_requests'))
    
    template = 'product_requests/confirm_delete_product_request.html'
    context = {
        'product_request': product_request,
    }

    return render(request, template, context)


@login_required
def delete_product_request(request, product_request_id):
    """ Delete a product request """
    product_request = get_object_or_404(ProductRequest, pk=product_request_id)
    if not request.user == product_request.created_by:
        messages.error(request, 'Sorry, you can only delete product requests you have \
                       written!')
        return redirect(reverse('product_requests'))
    product_request.delete()
    messages.success(request, 'Product request deleted!')
    return redirect(reverse('product_requests'))


@login_required
def add_product_request(request):
    """ Add a product_request """
    if request.method == 'POST':
        form = AddProductRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product request!')
            return redirect(reverse('product_requests'))
        else:
            messages.error(request, 'Failed to add product request. Please ensure the \
                           form is valid!')
    else:
        form = AddProductRequestForm(initial={
            'created_by': request.user,
        })

    template = 'product_requests/add_product_request.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

