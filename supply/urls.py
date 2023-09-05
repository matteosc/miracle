from django.urls import path

from . import views

urlpatterns = [
    path('arrivo/', views.create_arrivo_view, name='create-arrivo'),


]
