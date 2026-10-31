# Install

```shell
pip install django-food-recipes
```

Until sibling packages are on PyPI, CI/install may resolve `django-ingredients`
from GitHub (see `pyproject.toml`).

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
