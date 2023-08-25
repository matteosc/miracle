from datetime import datetime

from django.db import models

from personnel.models import Personnel



class Category(models.Model):
    """
    model for ingredinet that belong to a category
    """
    name = models.CharField(max_length=30)

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name



class Nutritionals(models.Model):
    """
    data extension for ingredient one to one relationship
    """
    calories = models.FloatField()
    carbohydrates = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()
    starch = models.FloatField()

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutritional = models.OneToOneField(Nutritionals,  on_delete=models.CASCADE)

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' (' + self.category.name + ')'




class OrdineCucina(models.Model):
    date = models.DateField(default=datetime.now)
    status= models.CharField(max_length=20)
    richiedente = models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True)
    note= models.TextField(null=True)



class VociOrdineCucina(models.Model):
    """
    items  for ordini cucina
    """
    ordine = models.ForeignKey(OrdineCucina, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    um= models.CharField(max_length=20)
    quantity = models.FloatField()
    note= models.TextField()

class Recipe(models.Model):
    name= models.CharField(max_length=80)
    servings= models.IntegerField()
    directions= models.TextField()
    createdOn= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class RecipeItem(models.Model):
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    quantityInGrOrMl= models.FloatField()

