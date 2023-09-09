from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import ArrivoFood, Article

def create_arrivo_view(request):

    context={}
    return render(request,'supply/createarrivo.html', context)
def articoliMain_view(request):
    articoli= Article.objects.all().order_by('name')
    context={'object_list': articoli}
    return render(request,'supply/articles.html', context)

