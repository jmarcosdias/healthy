from django import forms
from .models import NewsletterSubscription


class NewsletterForm(forms.ModelForm):
    """ Newsletter model form """

    class Meta:
        """ Defines the model and the fields to include """
        model = NewsletterSubscription
        fields = ('email',)
