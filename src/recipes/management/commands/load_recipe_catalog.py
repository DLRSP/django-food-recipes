"""Placeholder catalog command — recipe content is not seeded in this package."""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Recipe content is intentionally not shipped. Taxonomy rows are created "
        "by the consumer or admin; this command only confirms the package policy."
    )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING(
                "No recipe fixtures are packaged. Use admin or consumer imports "
                "for Diet/Cooking/Type/Recipe rows."
            )
        )
