"""
Reviews views here
"""


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm, AddReviewForm


@login_required
def all_reviews(request):
    """ A view to show all reviews """

    reviews = Review.objects.filter(created_by=request.user)

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/reviews.html', context)


@login_required
def edit_review(request, review_id):
    """ Edit a review """
    review = get_object_or_404(Review, pk=review_id)
    if not request.user == review.created_by:
        messages.error(request, 'Sorry, you can only edit reviews you have \
                       written!')
        return redirect(reverse('reviews'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to update review. Please ensure \
                                     the form is valid!')
    else:
        form = ReviewForm(instance=review)
        if review.product.subtitle:
            messages.info(request, f'You are editing a review for \
                          {review.product.title} - {review.product.subtitle}!')
        else:
            messages.info(request, f'You are editing a review for {review.product.title}!')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def confirm_delete_review(request, review_id):
    """ Confirm deletion of a review """
    review = get_object_or_404(Review, pk=review_id)
    if not request.user == review.created_by:
        messages.error(request, 'Sorry, you can only delete reviews you have \
                       written!')
        return redirect(reverse('reviews'))
    
    template = 'reviews/confirm_delete_review.html'
    context = {
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    review = get_object_or_404(Review, pk=review_id)
    if not request.user == review.created_by:
        messages.error(request, 'Sorry, you can only delete reviews you have \
                       written!')
        return redirect(reverse('reviews'))
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('reviews'))


@login_required
def add_review(request):
    """ Add a review """
    if request.method == 'POST':
        form = AddReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the \
                           form is valid!')
    else:
        form = AddReviewForm(initial={
            'created_by': request.user,
        })

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

