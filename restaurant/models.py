from django.db import models

class Dish(models.Model):
    TYPE_CHOICES = (
        ('A', 'Antipasti'),
        ('P', 'Primi'),
        ('S', 'Secondi'),
        ('D', 'Dessert'),
    )
    name= models.CharField(max_length=80)
    tipo = models.CharField(max_length=1, choices=TYPE_CHOICES)
    def __str__(self):
        return self.name

class Menu(models.Model):
    name= models.CharField(max_length=50, blank=True, null=True)
    activeFrom= models.DateField(null=True)
    activeTo= models.DateField(null=True)

class MenuItems(models.Model):
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    price=models.FloatField()

    def __str__(self):
        return self.dish.name