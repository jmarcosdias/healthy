"""
Here we will register the product models
"""


from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    """ Category as it appears in django admin module """
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    """ Product as it appears in django admin module """
    list_display = (
        'sku',
        'title',
        'subtitle',
        'category',
        'price',
        'image',
    )
    ordering = ('title',)


# Register the models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
