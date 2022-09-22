"""
Registration of newsletter models
"""


from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """
    Definition for the newsletter subscription as it appears on admin
    """

    readonly_fields = ('creation_date_time',)

    fields = ('email', 'creation_date_time')

    list_display = ('email', 'creation_date_time')
    
    ordering = ('-creation_date_time', 'email',)


admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
