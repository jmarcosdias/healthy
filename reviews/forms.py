from django import forms
from .models import Review
from products.models import Product


class ReviewForm(forms.ModelForm):
    """ Reviews model form """

    class Meta:
        """ Defines the model and the fields to include """
        model = Review
        fields = ('text_content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].label = ""


class AddReviewForm(forms.ModelForm):
    """ Reviews model form """

    class Meta:
        """ Defines the model and the fields to include """
        model = Review
        fields = ('product', 'text_content', 'created_by')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].label = "Your review"
        self.fields['created_by'].widget = forms.HiddenInput()
