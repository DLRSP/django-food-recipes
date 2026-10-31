from modeltranslation.translator import TranslationOptions, register

from recipes.models import (
    Cooking,
    Diet,
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


@register(Diet)
class DietTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(Cooking)
class CookingTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(RecipeOrigin)
class RecipeOriginTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(Type)
class TypeTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(SubType)
class SubTypeTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(RecipeYieldUnit)
class RecipeYieldUnitTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(RecipeCategory)
class RecipeCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ("title", "slug", "aphorism", "aphorism_author")


@register(RecipeStepName)
class RecipeStepNameTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(RecipeStep)
class RecipeStepTranslationOptions(TranslationOptions):
    fields = ("step",)


@register(RecipeTip)
class RecipeTipTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(RecipeAlternative)
class RecipeAlternativeTranslationOptions(TranslationOptions):
    fields = ("description",)
