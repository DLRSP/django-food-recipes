"""URL patterns for django-food-recipes (translated path prefixes)."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import path
from django.utils.translation import gettext_lazy as _

from recipes.models import (
    Cooking,
    Diet,
    Recipe,
    RecipeCategory,
    SubType,
    Type,
)


def diet_list(request):
    names = ", ".join(Diet.objects.order_by("name").values_list("name", flat=True))
    return HttpResponse(names or "diets")


def diet_detail(request, slug_diet):
    obj = get_object_or_404(Diet, slug=slug_diet)
    return HttpResponse(obj.name)


def cooking_list(request):
    names = ", ".join(Cooking.objects.order_by("name").values_list("name", flat=True))
    return HttpResponse(names or "cooking")


def cooking_detail(request, slug_cook):
    obj = get_object_or_404(Cooking, slug=slug_cook)
    return HttpResponse(obj.name)


def type_list(request):
    names = ", ".join(Type.objects.order_by("name").values_list("name", flat=True))
    return HttpResponse(names or "types")


def type_detail(request, slug_type):
    obj = get_object_or_404(Type, slug=slug_type)
    return HttpResponse(obj.name)


def subtype_detail(request, slug):
    obj = get_object_or_404(SubType, slug=slug)
    return HttpResponse(obj.name)


def category_list(request):
    names = ", ".join(
        RecipeCategory.objects.order_by("name").values_list("name", flat=True)
    )
    return HttpResponse(names or "categories")


def category_detail(request, slug_cat):
    obj = get_object_or_404(RecipeCategory, slug=slug_cat)
    return HttpResponse(obj.name)


def recipe_detail(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    return HttpResponse(obj.title)


urlpatterns = [
    path(_("diets/"), diet_list, name="diets"),
    path(_("diets/<slug:slug_diet>/"), diet_detail, name="diet-detail"),
    path(_("cooking/"), cooking_list, name="cookings"),
    path(_("cooking/<slug:slug_cook>/"), cooking_detail, name="cooking-detail"),
    path(_("types/"), type_list, name="type"),
    path(_("types/<slug:slug_type>/"), type_detail, name="type-detail"),
    path(_("subtypes/<slug:slug>/"), subtype_detail, name="subtype-detail"),
    path(_("categories/"), category_list, name="categories"),
    path(
        _("categories/<slug:slug_cat>/"), category_detail, name="category-detail"
    ),
    path(_("recipes/<slug:slug>/"), recipe_detail, name="recipe-detail"),
]
