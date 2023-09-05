from django.contrib import admin
from .models import Dish, Menu, MenuItems

class MenuAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu, MenuAdmin)

class MenuItemsAdmin(admin.ModelAdmin):
    pass

admin.site.register(MenuItems, MenuItemsAdmin)


class DishAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dish, DishAdmin)
