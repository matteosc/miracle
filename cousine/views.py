from django.shortcuts import render, redirect
from .models import Ingredient, Category
from .forms import IngredientForm, NutritionalForm


def ingredients_view(request):
    categories = Category.objects.order_by('name')
    ingredients = Ingredient.objects.order_by('name')
    context = {'categories': categories, 'ingredients': ingredients}
    return render(request, 'cousine/ingredients.html', context)

def category_ingredients_view(request, pk):
    categories = Category.objects.order_by('name')
    category=Category.objects.get(id=pk)

    ingredients=Ingredient.objects.filter(category__id=category.id).order_by('name')
    context={'categories': categories,'category': category, 'ingredients': ingredients }
    return render(request,'cousine/ingredients.html', context )

def ingredientDetalilview(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    context = {'object': ingredient}
    return render(request, 'cousine/ingredient_detail.html', context)


def ingredientCreateView(request):
    form1 = IngredientForm(request.POST or None)
    form2 = NutritionalForm(request.POST or None)

    if form1.is_valid() and form2.is_valid():
        ingredient = form1.save(commit=False)
        nutritionals = form2.save()
        ingredient.nutritional = nutritionals
        ingredient.save()
        print('inside valis')
        return redirect('cousine/ingredients/')
    context = {'form1': form1, 'form2': form2, }
    return render(request, 'cousine/ingredient_create.html', context)


def ingredientEditView(request, pk):
    ing = Ingredient.objects.get(id=pk)
    form1 = IngredientForm(request.POST or None, instance=ing)
    form2 = NutritionalForm(request.POST or None, instance=ing.nutritional)
    if form1.is_valid() and form2.is_valid():
        ingredient = form1.save(commit=False)
        nutritionals = form2.save()
        ingredient.nutritional = nutritionals
        ingredient.save()
        print('inside valis')
        return redirect('/cousine/ingredients/')
    context = {'form1': form1, 'form2': form2, }
    return render(request, 'cousine/ingredient_create.html', context)
