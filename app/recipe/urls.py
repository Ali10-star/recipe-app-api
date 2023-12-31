"""
URL mappings for the recipe app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views as RecipeViews


router = DefaultRouter()
router.register('recipes', viewset=RecipeViews.RecipeViewSet)
router.register('tags', viewset=RecipeViews.TagViewSet)
router.register('ingredients', viewset=RecipeViews.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
