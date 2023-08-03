from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blogs'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
