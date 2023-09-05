from django.shortcuts import render
from .models import Ingredient, Nutritionals, Category
from utilities.import_tools import import_categories, import_ingredients, import_suppliers

def ingredients_view(request):


    categories=Category.objects.order_by('name')
    ingredients=Ingredient.objects.order_by('name')
    context={'categories': categories, 'ingredients': ingredients }
    return render(request,'cousine/ingredients.html', context )

def ingredientDetalilview(request, pk):
    ingredient=Ingredient.objects.get(id=pk)
    context={ 'object': ingredient}
    return render(request,'cousine/ingredient_detail.html', context )

