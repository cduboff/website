from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('search/<int:id>', views.searchByid),
    path('submit', views.submit),
    path('response', views.response),
    path('create_meal_plan', views.create),
]