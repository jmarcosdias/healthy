from django import forms
from .models import ContactRequest


class DateInput(forms.DateInput):
    """ Used to make it easier for the user to choose a date """
    input_type = 'date'


class ContactRequestForm(forms.ModelForm):
    """ Contact requests model form """

    class Meta:
        """ Defines the model and the fields to include """
        model = ContactRequest
        fields = ('text_content',
                  'full_name',
                  'phone_number',
                  'contact_date',
                  'contact_timeslot')
        widgets = {
            'contact_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].label = 'Please give us an idea of \
            what you would like to hear from us about.'


class AddContactRequestForm(forms.ModelForm):
    """ Contact requests model form for adding a contact request"""

    class Meta:
        """ Defines the model and the fields to include """
        model = ContactRequest
        fields = ('text_content',
                  'full_name',
                  'phone_number',
                  'contact_date',
                  'contact_timeslot',
                  'created_by')
        widgets = {
            'contact_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].label = 'Please give us an idea of \
            what you would like to hear from us about.'
        self.fields['created_by'].widget = forms.HiddenInput()

