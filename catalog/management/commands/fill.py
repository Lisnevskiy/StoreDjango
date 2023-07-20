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
                    categories_for_create.append(Category(item['pk'], **item['fields']))

            Category.objects.bulk_create(categories_for_create)

            for item in data:
                if item['model'] == 'catalog.product':
                    item['fields']['category'] = Category.objects.get(pk=item['fields']['category'])
                    products_for_create.append(Product(item['pk'], **item['fields']))

            Product.objects.bulk_create(products_for_create)
