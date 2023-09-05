from django.shortcuts import render
import os
from supply.models import Article
from cousine.models import Ingredient
from utilities.import_tools import import_articles,import_categories,import_ingredients,import_suppliers
def home(request):
    """
    function respond to website rootHTTP request

    :param request:
    :return: index.html no db data yet
    """

    context={}
    return render(request, "restaurant/home.html", context)
