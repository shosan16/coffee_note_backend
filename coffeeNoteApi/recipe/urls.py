from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipeListViewSet.as_view()),
    path("<pk>", views.RecipeViewSet.as_view()),
]
