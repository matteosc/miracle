from django import forms
from .models import Ingredient, Nutritionals

class IngredientForm(forms.ModelForm):
    class Meta:
        model=Ingredient
        fields=['name', 'category']

class NutritionalForm(forms.ModelForm):
    class Meta:
        model=Nutritionals
        fields='__all__'