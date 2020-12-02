from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('search/<int:id>', views.searchByid),
    path('submit', views.submit),
    path('response', views.response),
    path('create_meal_plan', views.create),
    path('register', views.register),
    path('login', views.login),
    path('user_home', views.user_home),
    path('get_similar/<int:id>', views.similar_recipe),
    path('like/<int:id>', views.like),
    path('logout', views.logout),
    path('find_recipe/<int:id>', views.find_recipe),
    path('connect_user', views.connect_user),
    path('connect_form', views.connect_form),
]