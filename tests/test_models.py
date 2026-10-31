"""Model tests for django-food-recipes (core only, no content fixtures)."""

from __future__ import annotations

from importlib import resources
from pathlib import Path

from django.core.management import call_command
from django.db import connection
from django.test import TestCase

from ingredients.models import Ingredient, IngredientCategory, IngredientType
from recipes.constants import IQ_GROUP, IQ_UNIT
from recipes.models import (
    Diet,
    IngredientQuantity,
    Recipe,
    RecipeCategory,
    RecipeStep,
    Type,
)


class RecipeModelTests(TestCase):
    def test_default_table_names(self):
        self.assertEqual(Recipe._meta.db_table, "recipes_recipe")
        self.assertEqual(Diet._meta.db_table, "recipes_diet")
        self.assertEqual(
            IngredientQuantity._meta.db_table, "recipes_ingredientquantity"
        )
        self.assertEqual(RecipeStep._meta.db_table, "recipes_recipestep")

    def test_no_recipe_fixtures_in_package(self):
        data_dir = Path(resources.files("recipes")) / "data"
        self.assertFalse(data_dir.exists())
        pkg_root = Path(resources.files("recipes"))
        json_files = list(pkg_root.rglob("*.json"))
        self.assertEqual(json_files, [])

    def test_english_choice_codes(self):
        group_codes = {c[0] for c in IQ_GROUP if c[0]}
        self.assertIn("decoration", group_codes)
        self.assertIn("dough", group_codes)
        self.assertNotIn("Per la decorazione", group_codes)
        unit_codes = {c[0] for c in IQ_UNIT if c[0]}
        self.assertIn("tablespoon", unit_codes)
        self.assertNotIn("cucchiaio", unit_codes)

    def test_create_recipe_with_quantity(self):
        itype = IngredientType.objects.create(name="Dairy", slug="dairy")
        cat = IngredientCategory.objects.create(
            name="Milk products", slug="milk-products", type=itype
        )
        ingredient = Ingredient.objects.create(
            name="Milk", slug="milk", category=cat
        )
        rtype = Type.objects.create(name="Main", slug="main")
        rcat = RecipeCategory.objects.create(name="Pasta", slug="pasta")
        recipe = Recipe.objects.create(
            title="Test Pasta",
            slug="test-pasta",
            category=rcat,
            type=rtype,
            aphorism="Cook with care",
            published=True,
        )
        IngredientQuantity.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            group="dough",
            quantity="100",
            quantity_unit="g",
        )
        RecipeStep.objects.create(
            recipe=recipe, step_number=1, step="Boil water."
        )
        self.assertEqual(recipe.ingredient_quantities.count(), 1)
        self.assertEqual(recipe.steps.count(), 1)
        self.assertIn("/recipes/test-pasta/", recipe.get_absolute_url())

    def test_core_recipe_has_no_seo_or_social_fields(self):
        field_names = {f.name for f in Recipe._meta.get_fields()}
        forbidden = {
            "bing_indexing",
            "share_instagram",
            "share_facebook",
            "share_twitter",
            "social_title",
            "referrals",
            "tags",
            "allow_comments",
            "votes",
        }
        self.assertTrue(forbidden.isdisjoint(field_names))

    def test_load_recipe_catalog_is_noop(self):
        call_command("load_recipe_catalog")
        self.assertEqual(Recipe.objects.count(), 0)

    def test_migrated_tables_use_recipes_prefix(self):
        with connection.cursor() as cursor:
            tables = connection.introspection.table_names(cursor)
        self.assertIn("recipes_recipe", tables)
        self.assertNotIn("recipes_ingredient", tables)
