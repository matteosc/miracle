from django.db import models
from django.urls import reverse
from cousine.models import Ingredient


class Recipe(models.Model):
    name= models.CharField(max_length=80)
    servings= models.IntegerField()
    directions= models.TextField()
    createdOn= models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'id':self.id})

    def __str__(self):
        return self.name

class RecipeItem(models.Model):
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    quantityInGrOrMl= models.FloatField()
