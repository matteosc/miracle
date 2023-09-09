from django.urls import path, include,reverse

from . import views

app_name='recipes'
urlpatterns = [

    path('', views.recepy_list_view, name='list'),


    path('create/', views.recepy_create_view, name='create'),

    path('<int:id>/edit', views.recepy_update_view, name='update'),

    path('<int:id>/', views.recepy_detail_view, name='detail'),

]