from django.urls import path, include

from . import views

urlpatterns = [
    path('ingredients/', views.ingredients_view, name='ingredient-main'),
    path('ingredients/category/<int:pk>/', views.category_ingredients_view, name='category-ingredients'),
    path('ingredients/<int:pk>/', views.ingredientDetalilview, name='ingredient-detail'),
    path('ingredients/<int:pk>/edit', views.ingredientEditView, name='ingredient-edit'),
    path('ingredients/create', views.ingredientCreateView, name='ingredient-create'),

]
