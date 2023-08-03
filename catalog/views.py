from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Товары'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Страница товара'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}
