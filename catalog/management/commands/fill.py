from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        catalog_list = [
            {'name': 'Виджет', 'description': 'Описание виджета'},
            {'name': 'Сайт', 'description': 'Описание сайта'},
            {'name': 'Бар', 'description': 'Описание бара'},
            {'name': 'Реклама', 'description': 'Описание рекламы'},
            {'name': 'Верстка', 'description': 'Описание верстки'},
            {'name': 'Консультации', 'description': 'Описание консультации'},
        ]

        for catalog_item in catalog_list:
            categore_for_create = []
            categore_for_create.append(Category(**catalog_item))
        Category.objects.bulk_create(categore_for_create)