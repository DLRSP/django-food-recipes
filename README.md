# django-food-recipes

[![CI](https://github.com/DLRSP/django-food-recipes/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-food-recipes/actions/workflows/ci.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Core recipe models for Django: taxonomy (diet, cooking, type, category),
recipe steps, tips, alternatives, and ingredient quantities. Depends on
`django-ingredients` (and transitively `django-allergens`). Uses django-filer
for images and modeltranslation for translatable fields.

**No recipe content fixtures** ship in this package — only catalog dependencies
live upstream.

## Requirements

- Python 3.10+
- Django 4.2+
- django-ingredients
- django-filer
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
    "allergens",
    "ingredients",
    "recipes",
]
```

```shell
python manage.py migrate
```

## Scope notes

Core only: times, yield, nutrition integers, publish flags, aphorism, Filer
image. SEO/social/referral/tags/flags/comments stay in the consumer site.

Quantity `group` / `quantity_unit` values are English stable codes; Italian
labels are in `locale/it`.

## License

MIT
