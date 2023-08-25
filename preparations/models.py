from django.db import models

from cousine.models import Recipe
from supply.models import Article


# Create your models here.
class Preparation(models.Model):
    recipe= models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)

    date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class PreparationItem(models.Model):
    preparation= models.ForeignKey(Preparation, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantityInGrOrMl= models.FloatField()
    scarto=models.FloatField()
    caloPonderale=models.FloatField()
    costoAlGr=models.FloatField()
