import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        categories_for_create = []
        products_for_create = []

        with open('catalog_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                if item['model'] == 'catalog.category':
                    categories_for_create.append(Category(**item['fields']))
                # elif item['model'] == 'catalog.product':
                #     products_for_create.append(Product(**item['fields']))

        Category.objects.bulk_create(categories_for_create)
        # Product.objects.bulk_create(products_for_create)
