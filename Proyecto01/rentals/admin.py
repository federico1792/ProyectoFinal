from django.contrib import admin

from rentals.models import Rental

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('title', 'zone', 'price', 'environments', 'toilets', 'sold',)
    list_filter = ('sold',)
    search_fields = ('zone', 'environments',)
