from django.shortcuts import render, get_object_or_404,redirect
from .models import Recipe,RecipeItem
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
def recepy_list_view(request, id=None):
    qs=Recipe.objects.all()
    context={
        'object_list':qs
    }
    return render(request, 'recipes/list.html',context)
def recepy_detail_view(request, id=None):
    obj=get_object_or_404(Recipe, id=id)# can add es user=..
    context={
        'object':obj
    }
    return render(request, 'recipes/detail.html',context)

@login_required
def recepy_create_view(request):
    form=RecipeForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        obj=form.save(commit=False)
        # user=request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html',context)

def recepy_update_view(request, id=None):
    obj=get_object_or_404(Recipe, id=id)
    form=RecipeForm(request.POST or None, instance=obj)
    context={
        'object':obj,
        'form':form,
    }
    if form.is_valid():
        form.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html',context)
