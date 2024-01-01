from django.contrib import admin
from .models import Reservation
from .models import UIElement


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name', 'last_name', 'email',
        'date', 'time', 'party_size', 'phone', 'created_at'
    )
    list_filter = (
        'date', 'time', 'created_at'
    )
    search_fields = (
        'user__username', 'first_name', 'last_name',
        'email', 'phone'
    )


@admin.register(UIElement)
class UIElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
