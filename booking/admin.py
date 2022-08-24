from django.contrib import admin

from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'car', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'car')
    list_per_page = 15

admin.site.register(Booking, BookingAdmin)
