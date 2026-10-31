# django-food-recipes

Template repository for a **reusable Django app** published on PyPI. After you clone and rename, replace the placeholder import package `recipes` and the distribution name `django-food-recipes` across the tree (see the checklist in `README.md`).

---

## Requirements

- Python 3.10+
- Django 3.2+ (see `pyproject.toml` for declared compatibility)

---

## Installation

```shell
pip install django-food-recipes
```

Add the app to `INSTALLED_APPS` using your real module name (after renaming from `recipes`):

```python
INSTALLED_APPS = [
    # ...
    "recipes",
    # ...
]
```

---

## Documentation

Full docs are built with [MkDocs](https://www.mkdocs.org/) (Material theme). From the repo root:

```shell
pip install -e ".[docs]"
mkdocs serve
```
