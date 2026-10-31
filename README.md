# django-food-recipes

[![CI](https://github.com/DLRSP/django-food-recipes/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-food-recipes/actions/workflows/ci.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/docs-github.io-blue)](https://dlrsp.github.io/django-food-recipes/)

Reusable **recipe domain models** for Django: diets, cooking methods, types,
categories, steps, tips, alternatives, and ingredient quantities.

## Why use it

- Model complete recipes without reinventing taxonomy and quantity links
- Connect to the shared ingredient and allergen catalogs
- Multilingual public routes (English default; Italian prefixes such as
  `ricette/`, `diete/`)
- Image fields via django-filer for admin and site presentation

Recipe **content** is owned by your site — this package provides the schema and
integration points, not editorial fixtures.

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
