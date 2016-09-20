from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter(schema_title='Recipes')
router.register(r'recipes', views.RecipeViewSet)
router.register(r'reported', views.ReportedRecipeViewSet)
router.register(r'stored', views.StoredRecipeViewSet)
router.register(r'noted', views.NoteRecipeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]