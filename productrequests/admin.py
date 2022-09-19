"""
Registration of product requests models
"""


from django.contrib import admin
from .models import ProductRequest


class ProductRequestAdmin(admin.ModelAdmin):
    """
    Definition for the product request as it appears on admin
    """
    readonly_fields = ('creation_date_time', 'last_update_date_time')

    fields = ('created_by', 'text_content', 'creation_date_time',
              'last_update_date_time')

    list_display = ('created_by', 'text_content',
                    'creation_date_time', 'last_update_date_time')
    
    ordering = ('-last_update_date_time', 'created_by__username', )


admin.site.register(ProductRequest, ProductRequestAdmin)
