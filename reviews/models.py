"""
Models definitions for the reviews app
"""


from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Definition of the review model
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False,
                                blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                                   blank=False)
    text_content = models.TextField(null=False, blank=False)
    creation_date_time = models.DateTimeField(auto_now_add=True)
    last_update_date_time = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Inner meta class of reviews. Used to change the default ordering.
        """
        ordering = ['-creation_date_time', 'created_by__username']

    def __str__(self):
        return f'Review #{self.id}'
