from django.contrib import admin

from cousine.models import Category, Ingredient, OrdineCucina, VociOrdineCucina
from recipes.models import Recipe, RecipeItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    def get_ordering(self, request):
        return ['id']  # sort case insensitive

admin.site.register(Category, CategoryAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    search_fields = ['name']
    def get_ordering(self, request):
        return ['name']  # sort case insensitive


admin.site.register(Ingredient, IngredientAdmin)

class OrdineCucinaAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrdineCucina, OrdineCucinaAdmin)

class VociOrdineCucinaAdmin(admin.ModelAdmin):
    pass

admin.site.register(VociOrdineCucina, VociOrdineCucinaAdmin)


class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)

class RecipeItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecipeItem, RecipeItemAdmin)


