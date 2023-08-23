from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' (' + self.category.name + ')'
