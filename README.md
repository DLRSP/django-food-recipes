# django-food-recipes

[![CI](https://github.com/DLRSP/django-food-recipes/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-food-recipes/actions/workflows/ci.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/docs-github.io-blue)](https://dlrsp.github.io/django-food-recipes/)

Core recipe models for Django: taxonomy (diet, cooking, type, category),
recipe steps, tips, alternatives, and ingredient quantities. Depends on
`django-ingredients` (and transitively `django-allergens`). Uses django-filer
for images and modeltranslation for translatable fields.

**No recipe content fixtures** ship in this package — only catalog dependencies
live upstream.

Default language is **English**. Italian URL prefixes (`ricette/`, `diete/`, …)
ship via gettext.

## Requirements

- Python 3.10+
- Django 4.2+
- django-ingredients
- django-filer (+ mptt, easy-thumbnails, polymorphic)
- django-modeltranslation

## Install

```shell
pip install django-food-recipes
```

```python
INSTALLED_APPS = [
    "modeltranslation",
    # ...
    "easy_thumbnails",
    "filer",
    "mptt",
    "polymorphic",
    "allergens",
    "ingredients",
    "recipes",
]
```

```shell
python manage.py migrate
```

Include `recipes.urls` inside `i18n_patterns` for translated path prefixes.

## License

MIT
