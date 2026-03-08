from django.contrib import admin
from .models import Registration
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at', 'is_paid_display', 'payment_transaction')
    actions = ['confirm_payment']

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Name'

    def is_paid_display(self, obj):
        if obj.is_paid:
            return format_html('<span style="background-color: green; color: white; padding: 5px; border-radius: 3px;">{}</span>', "Confirmed")
        else:
            return format_html('<span style="background-color: red; color: white; padding: 5px; border-radius: 3px;">{}</span>', "Pending")
    is_paid_display.short_description = 'Payment Status'

    @admin.action(description='Confirm Payment')
    def confirm_payment(self, request, queryset):
        for registration in queryset:
            registration.is_paid = not registration.is_paid
            registration.save()

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/confirm_payment/', self.admin_site.admin_view(self.toggle_payment), name='registration-confirm-payment'),
        ]
        return custom_urls + urls

    def toggle_payment(self, request, pk):
        registration = self.get_object(request, pk)
        registration.is_paid = not registration.is_paid
        registration.save()
        self.message_user(request, f"Payment status for {registration.full_name()} has been updated.")
        return redirect('..')

admin.site.register(Registration, RegistrationAdmin)
