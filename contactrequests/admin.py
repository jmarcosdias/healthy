"""
Registration of contact requests models
"""


from django.contrib import admin
from .models import ContactRequest


class ContactRequestAdmin(admin.ModelAdmin):
    """
    Definition for the contact request as it appears on admin
    """
    readonly_fields = ('creation_date_time', 'last_update_date_time')

    fields = ('contact_date', 'contact_timeslot', 'full_name',
              'phone_number', 'text_content', 'created_by', 
              'creation_date_time', 'last_update_date_time')              

    list_display = ('contact_date', 'contact_timeslot', 'full_name',
                    'phone_number', 'created_by',
                    'creation_date_time', 'last_update_date_time')
    
    ordering = ('-contact_date', '-contact_timeslot',
                'created_by__username',)


admin.site.register(ContactRequest, ContactRequestAdmin)
