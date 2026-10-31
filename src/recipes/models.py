import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from recipes.constants import IQ_GROUP, IQ_UNIT

not_negative = MinValueValidator(0)


class Diet(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True)
    schema_tag = models.CharField(_("Restricted diet"), max_length=15, blank=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="diet_images",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Diet")
        verbose_name_plural = _("Diets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("diet-detail", kwargs={"slug_diet": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Cooking(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="cooking_images",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Cooking method")
        verbose_name_plural = _("Cooking methods")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cooking-detail", kwargs={"slug_cook": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class RecipeOrigin(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="recipe_origin_images",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Recipe origin")
        verbose_name_plural = _("Recipe origins")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Type(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="recipe_type_images",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Recipe type")
        verbose_name_plural = _("Recipe types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type-detail", kwargs={"slug_type": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class SubType(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="recipe_subtype_images",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Recipe sub-type")
        verbose_name_plural = _("Recipe sub-types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subtype-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class RecipeYieldUnit(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Recipe yield unit")
        verbose_name_plural = _("Recipe yield units")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class RecipeCategory(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    type = models.ManyToManyField(Type, verbose_name=_("Types"), blank=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="recipe_category_images",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Recipe category")
        verbose_name_plural = _("Recipe categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug_cat": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class RecipeTip(models.Model):
    description = models.TextField(_("Description"), max_length=5000)

    class Meta:
        verbose_name = _("Recipe tip")
        verbose_name_plural = _("Recipe tips")

    def __str__(self):
        return self.description[:80]


class RecipeAlternative(models.Model):
    description = models.TextField(_("Description"), max_length=5000)
    suitable_for_diet = models.ManyToManyField(
        Diet, verbose_name=_("Suitable for diet"), blank=True
    )

    class Meta:
        verbose_name = _("Recipe alternative")
        verbose_name_plural = _("Recipe alternatives")

    def __str__(self):
        return self.description[:80]


class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    category = models.ForeignKey(
        RecipeCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    type = models.ForeignKey(
        Type,
        verbose_name=_("Type"),
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    sub_type = models.ForeignKey(
        SubType,
        verbose_name=_("Sub-type"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes",
    )
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient",
        through="IngredientQuantity",
        related_name="recipes",
        verbose_name=_("Ingredients"),
    )
    suitable_for_diet = models.ManyToManyField(
        Diet, blank=True, verbose_name=_("Suitable for diet")
    )
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="recipe_images",
    )
    aphorism = models.TextField(_("Aphorism"), max_length=500, blank=True)
    aphorism_author = models.CharField(
        _("Aphorism author"), max_length=350, null=True, blank=True, default="Anonymous"
    )
    cooking = models.ManyToManyField(
        Cooking, blank=True, verbose_name=_("Cooking methods")
    )
    cooking_time = models.IntegerField(_("Cooking time"), blank=True, default=0)
    preparation_time = models.IntegerField(
        _("Preparation time"), blank=True, default=0
    )
    recipe_yield = models.IntegerField(_("Yield quantity"), blank=True, default=4)
    recipe_yield_unit = models.ForeignKey(
        RecipeYieldUnit,
        verbose_name=_("Yield unit"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes",
    )
    origins = models.ForeignKey(
        RecipeOrigin,
        verbose_name=_("Origin"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes",
    )
    alternative = models.ManyToManyField(
        RecipeAlternative, blank=True, verbose_name=_("Alternatives")
    )
    tip = models.ManyToManyField(RecipeTip, blank=True, verbose_name=_("Tips"))

    create = models.DateTimeField(_("Created"), auto_now_add=True)
    publish = models.DateTimeField(_("Published at"), blank=True, null=True)
    modified = models.DateTimeField(_("Modified"), blank=True, null=True)
    published = models.BooleanField(_("Published"), default=False)

    calories = models.IntegerField(
        _("Calories [kcal]"), blank=True, null=True, validators=[not_negative]
    )
    carbohydrate = models.IntegerField(
        _("Carbohydrate [g]"), blank=True, null=True, validators=[not_negative]
    )
    sugar = models.IntegerField(
        _("Sugar [g]"), blank=True, null=True, validators=[not_negative]
    )
    fat = models.IntegerField(
        _("Fat [g]"), blank=True, null=True, validators=[not_negative]
    )
    saturatedfat = models.IntegerField(
        _("Saturated fat [g]"), blank=True, null=True, validators=[not_negative]
    )
    fiber = models.IntegerField(
        _("Fiber [g]"), blank=True, null=True, validators=[not_negative]
    )
    cholesterol = models.IntegerField(
        _("Cholesterol [mg]"), blank=True, null=True, validators=[not_negative]
    )
    sodium = models.IntegerField(
        _("Sodium (Na) [mg]"), blank=True, null=True, validators=[not_negative]
    )
    protein = models.IntegerField(
        _("Protein [g]"), blank=True, null=True, validators=[not_negative]
    )
    potassium = models.IntegerField(
        _("Potassium (K) [mg]"), blank=True, null=True, validators=[not_negative]
    )
    zinco = models.IntegerField(
        _("Zinc (Zn) [mg]"), blank=True, null=True, validators=[not_negative]
    )
    calcium = models.IntegerField(
        _("Calcium (Ca) [mg]"), blank=True, null=True, validators=[not_negative]
    )
    ferrum = models.IntegerField(
        _("Iron (Fe) [mg]"), blank=True, null=True, validators=[not_negative]
    )
    phosphorus = models.IntegerField(
        _("Phosphorus (P) [mg]"), blank=True, null=True, validators=[not_negative]
    )
    vit_a = models.IntegerField(
        _("Vitamin A (retinol) [μg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_a_eq = models.IntegerField(
        _("Retinol equivalents [μg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_a_beta = models.IntegerField(
        _("Beta-carotene [μg]"), blank=True, null=True, validators=[not_negative]
    )
    vit_b1 = models.IntegerField(
        _("Vitamin B1 (thiamine) [mg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_b2 = models.IntegerField(
        _("Vitamin B2 (riboflavin) [mg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_b3 = models.IntegerField(
        _("Vitamin B3 (niacin) [mg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_b6 = models.IntegerField(
        _("Vitamin B6 (pyridoxine) [mg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_b9 = models.IntegerField(
        _("Vitamin B9 (folic acid) [μg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_c = models.IntegerField(
        _("Vitamin C (ascorbic acid) [mg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_d = models.IntegerField(
        _("Vitamin D (cholecalciferol) [μg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )
    vit_e = models.IntegerField(
        _("Vitamin E (tocopherol) [mg]"),
        blank=True,
        null=True,
        validators=[not_negative],
    )

    class Meta:
        ordering = ["-publish", "title"]
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        if not self.publish:
            return False
        return self.publish >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def allergen_slugs(self):
        """Cascade allergen slugs from linked ingredients (present only)."""
        from ingredients.models import IngredientAllergenPresence

        return sorted(
            set(
                IngredientAllergenPresence.objects.filter(
                    ingredient__in=self.ingredients.all(),
                    present=True,
                ).values_list("allergen__slug", flat=True)
            )
        )


class RecipeStepName(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = _("Recipe step name")
        verbose_name_plural = _("Recipe step names")

    def __str__(self):
        return self.name


class RecipeStep(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name=_("Recipe"),
        on_delete=models.CASCADE,
        related_name="steps",
    )
    step_name = models.ForeignKey(
        RecipeStepName,
        verbose_name=_("Step name"),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="steps",
    )
    step_number = models.IntegerField(_("Step number"), default=1)
    step = models.TextField(_("Step text"), blank=True, null=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="recipe_step_images",
    )

    class Meta:
        ordering = ["recipe", "step_number"]
        verbose_name = _("Recipe step")
        verbose_name_plural = _("Recipe steps")

    def __str__(self):
        return self.step or f"Step {self.step_number}"


class IngredientQuantity(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name=_("Recipe"),
        on_delete=models.CASCADE,
        related_name="ingredient_quantities",
    )
    group = models.CharField(
        _("Group"),
        choices=IQ_GROUP,
        max_length=30,
        default="",
        blank=True,
    )
    ingredient = models.ForeignKey(
        "ingredients.Ingredient",
        verbose_name=_("Ingredient"),
        on_delete=models.CASCADE,
        related_name="quantities",
    )
    extra_info = models.CharField(
        _("Extra info"), max_length=50, default="", blank=True
    )
    quantity = models.CharField(_("Quantity"), max_length=5, default="q.b.")
    quantity_unit = models.CharField(
        _("Quantity unit"),
        choices=IQ_UNIT,
        max_length=15,
        default="",
        blank=True,
    )
    quantity_extra_info = models.CharField(
        _("Quantity extra info"), max_length=50, default="", blank=True
    )

    class Meta:
        verbose_name = _("Ingredient quantity")
        verbose_name_plural = _("Ingredient quantities")

    def __str__(self):
        return f"{self.quantity} {self.quantity_unit} {self.ingredient}".strip()
