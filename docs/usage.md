# Usage

```python
from recipes.models import Recipe

recipe = Recipe.objects.get(slug="test-pasta")
print(recipe.allergen_slugs())
```

Translated URL prefixes (via gettext + `i18n_patterns`):

| English | Italian |
|---------|---------|
| `diets/` | `diete/` |
| `cooking/` | `tipi-cottura/` |
| `types/` | `piatto/` |
| `categories/` | `categorie/` |
| `recipes/` | `ricette/` |
