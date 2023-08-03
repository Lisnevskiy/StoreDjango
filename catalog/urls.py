from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('products/<int:pk>/', products, name='products'),
    path('contacts/', contacts, name='contacts'),
]
