"""
Models definitions for newsletters
"""


# from datetime import date, datetime
from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator


class NewsletterSubscription(models.Model):
    """
    Definition of the newsletter subscription model
    """
    email = models.EmailField(max_length=254, null=False,
                              blank=False, unique=True)
    creation_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
