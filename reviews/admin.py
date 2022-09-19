"""
Registration of reviews models
"""


from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Definition for the review as it appears on admin
    """
    readonly_fields = ('creation_date_time', 'last_update_date_time')

    fields = ('product', 'created_by', 'text_content', 'creation_date_time',
              'last_update_date_time')

    list_display = ('product', 'created_by', 'text_content',
                    'creation_date_time', 'last_update_date_time')
    
    ordering = ('-last_update_date_time', 'created_by__username', )


admin.site.register(Review, ReviewAdmin)
