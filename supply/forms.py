from django import forms
from django.forms import inlineformset_factory
from .models import ArrivoFood, Article

class ArrivoFoodForm():
    class Meta:
        model = ArrivoFood
        fields = '__all__'
