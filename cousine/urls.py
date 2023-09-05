from django.urls import path, include

from . import views

urlpatterns = [
    path('ingredients/', views.ingredients_view, name='ingredient-main'),
    path('ingredients/<int:pk>/', views.ingredientDetalilview, name='ingredient-detail'),


]
