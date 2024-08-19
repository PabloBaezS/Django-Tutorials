from django.core.management.base import BaseCommand
from pages.factories import create_product

class Command(BaseCommand):
    help = 'Seed the database with products'

    def handle(self, *args, **kwargs):
        for _ in range(8):
            create_product()
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))
