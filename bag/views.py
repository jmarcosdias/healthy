from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    product_name = None

    if product.subtitle:
        product_name = '{product.title} - {product.subtitle}'
    else:
        product_name = product.title


    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product_name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product_name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
    

