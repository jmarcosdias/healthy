"""
Models definitions for the product requests app
"""


from django.db import models
from django.contrib.auth.models import User


class ProductRequest(models.Model):
    """
    Definition of the product request model
    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                                   blank=False)
    text_content = models.TextField(null=False, blank=False)
    creation_date_time = models.DateTimeField(auto_now_add=True)
    last_update_date_time = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Inner meta class of product requests. Used to change the default ordering.
        """
        ordering = ['-creation_date_time', 'created_by__username']

    def __str__(self):
        return f'Product request #{self.id}'
