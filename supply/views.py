from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import ArrivoFood

def create_arrivo_view(request):
    ArriviFormSet=modelformset_factory(ArrivoFood,fields=('incomingdate', 'article','quantity', 'price', 'conforme', 'scadenza') , extra=3)
    if request.method=='POST':
        form =ArriviFormSet(request.POST)
        return redirect('/')

    form =ArriviFormSet()
    context={'form': form, }
    return render(request,'supply/createarrivo.html', context)
