"""
Models definitions for the contact requests app
"""


from datetime import date
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class ContactRequest(models.Model):
    """
    Definition of the contact request model
    """
    TIME_SLOT_1 = 'S1'
    TIME_SLOT_2 = 'S2'
    TIME_SLOT_3 = 'S3'
    TIME_SLOT_4 = 'S4'
    TIME_SLOT_5 = 'S5'
    TIME_SLOT_6 = 'S6'
    TIME_SLOT_7 = 'S7'
    TIME_SLOT_8 = 'S8'
    TIME_SLOT_9 = 'S9'
    TIMESLOT_CHOICES = [
        (TIME_SLOT_1, '9am to 10am'),
        (TIME_SLOT_2, '10am to 11am'),
        (TIME_SLOT_3, '11am to 12pm'),
        (TIME_SLOT_4, '12pm to 1pm'),
        (TIME_SLOT_5, '1pm to 2pm'),
        (TIME_SLOT_6, '2pm to 3pm'),
        (TIME_SLOT_7, '3pm to 4pm'),
        (TIME_SLOT_8, '4pm to 5pm'),
        (TIME_SLOT_9, '5pm to 6pm'),
    ]
    text_content = models.TextField(null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    contact_date = models.DateField(null=False, blank=False,
                                    validators=[MinValueValidator(
                                         limit_value=date.today
                                         )])
    contact_timeslot = models.CharField(max_length=2,
                                        choices=TIMESLOT_CHOICES,
                                        default=TIME_SLOT_1,
                                        unique_for_date="contact_date",
                                        error_messages={
                                            "unique_for_date": "Sorry \
                                            but this time slot is already \
                                            booked. Please try another \
                                            day or another time slot."})
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                                   blank=False)
    creation_date_time = models.DateTimeField(auto_now_add=True)
    last_update_date_time = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Inner meta class of contact requests.
        Used to change the default ordering.
        """
        ordering = ['-contact_date', '-contact_timeslot',
                    'created_by__username']

    def __str__(self):
        return f'Contact request #{self.id}'
