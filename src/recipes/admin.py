from django.contrib import admin

from recipes.models import (
    Cooking,
    Diet,
    IngredientQuantity,
    Recipe,
    RecipeAlternative,
    RecipeCategory,
    RecipeOrigin,
    RecipeStep,
    RecipeStepName,
    RecipeTip,
    RecipeYieldUnit,
    SubType,
    Type,
)


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    extra = 0
    autocomplete_fields = ("ingredient",)


class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    extra = 0


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "schema_tag")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(Cooking)
class CookingAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(RecipeOrigin)
class RecipeOriginAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(SubType)
class SubTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(RecipeYieldUnit)
class RecipeYieldUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")
    filter_horizontal = ("type",)


@admin.register(RecipeTip)
class RecipeTipAdmin(admin.ModelAdmin):
    search_fields = ("description",)


@admin.register(RecipeAlternative)
class RecipeAlternativeAdmin(admin.ModelAdmin):
    search_fields = ("description",)
    filter_horizontal = ("suitable_for_diet",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "type", "published", "publish")
    list_filter = ("published", "type", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug", "aphorism")
    filter_horizontal = (
        "suitable_for_diet",
        "cooking",
        "alternative",
        "tip",
    )
    inlines = [IngredientQuantityInline, RecipeStepInline]


@admin.register(RecipeStepName)
class RecipeStepNameAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ("recipe", "step_number", "step_name")
    list_filter = ("recipe",)
    search_fields = ("step", "recipe__title")


@admin.register(IngredientQuantity)
class IngredientQuantityAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "ingredient",
        "group",
        "quantity",
        "quantity_unit",
    )
    list_filter = ("group", "quantity_unit")
    search_fields = ("recipe__title", "ingredient__name")
    autocomplete_fields = ("recipe", "ingredient")
