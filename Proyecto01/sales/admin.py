from django.contrib import admin

from sales.models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'zone', 'price', 'environments', 'toilets', 'sold',)
    list_filter = ('sold',)
    search_fields = ('zone', 'environments',)
