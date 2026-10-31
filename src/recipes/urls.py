"""URL patterns for django-food-recipes."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import path

from recipes.models import (
    Cooking,
    Diet,
    Recipe,
    RecipeCategory,
    SubType,
    Type,
)


def diet_detail(request, slug_diet):
    obj = get_object_or_404(Diet, slug=slug_diet)
    return HttpResponse(obj.name)


def cooking_detail(request, slug_cook):
    obj = get_object_or_404(Cooking, slug=slug_cook)
    return HttpResponse(obj.name)


def type_detail(request, slug_type):
    obj = get_object_or_404(Type, slug=slug_type)
    return HttpResponse(obj.name)


def subtype_detail(request, slug):
    obj = get_object_or_404(SubType, slug=slug)
    return HttpResponse(obj.name)


def category_detail(request, slug_cat):
    obj = get_object_or_404(RecipeCategory, slug=slug_cat)
    return HttpResponse(obj.name)


def recipe_detail(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    return HttpResponse(obj.title)


urlpatterns = [
    path("diets/<slug:slug_diet>/", diet_detail, name="diet-detail"),
    path("cooking/<slug:slug_cook>/", cooking_detail, name="cooking-detail"),
    path("types/<slug:slug_type>/", type_detail, name="type-detail"),
    path("subtypes/<slug:slug>/", subtype_detail, name="subtype-detail"),
    path(
        "categories/<slug:slug_cat>/", category_detail, name="category-detail"
    ),
    path("recipes/<slug:slug>/", recipe_detail, name="recipe-detail"),
]
