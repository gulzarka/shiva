from django.contrib import admin

from .models import Clarification, Client, Request, Subcontractor

@admin.register(Clarification)
class ClarificationAdmin(admin.ModelAdmin):
    search_fields = ['request__client', 'request__subcontractor', 'creation_date']
    readonly_fields = ['creation_date']
    list_display = (
        'request',
        'creation_date',
        'question',
        'answer',
    )
    list_filter = ['request__client', 'request__subcontractor']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    search_fields = ['client', 'subcontractor', 'creation_date']
    readonly_fields = ['creation_date']
    list_display = (
        'client',
        'subcontractor',
        'creation_date',
        'title',
        'price',
        'status',
        'difficulty',
    )
    list_filter = ['client', 'subcontractor', 'status', 'difficulty']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name', 'telegram_id', 'registration_date', 'subscription_end']
    readonly_fields = ['registration_date']
    list_display = (
        'name',
        'telegram_id',
        'registration_date',
        'subscription_end',
    )


@admin.register(Subcontractor)
class SubcontractorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'telegram_id', 'registration_date',]
    readonly_fields = ['registration_date']
    list_display = (
        'name',
        'telegram_id',
        'registration_date',
        'salary',
        'is_active',
    )
    list_filter = ['is_active']