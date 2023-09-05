from django.contrib import admin

from supply.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    def get_ordering(self, request):
        return ['name']  # sort case insensitive


admin.site.register(Supplier, SupplierAdmin)