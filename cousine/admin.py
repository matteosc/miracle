from django.contrib import admin

from cousine.models import Category, Ingredient


class CategoryAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['name']  # sort case insensitive

admin.site.register(Category, CategoryAdmin)

class IngredientAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['name']  # sort case insensitive


admin.site.register(Ingredient, IngredientAdmin)
