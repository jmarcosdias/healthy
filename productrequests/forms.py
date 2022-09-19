from django import forms
from .models import ProductRequest


class ProductRequestForm(forms.ModelForm):
    """ Product requests model form """

    class Meta:
        """ Defines the model and the fields to include """
        model = ProductRequest
        fields = ('text_content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].label = ""


class AddProductRequestForm(forms.ModelForm):
    """ Product requests model form for adding a product request"""

    class Meta:
        """ Defines the model and the fields to include """
        model = ProductRequest
        fields = ('text_content', 'created_by')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].label = "Please write here your request \
            for a product you would like to see in our store"
        self.fields['created_by'].widget = forms.HiddenInput()
