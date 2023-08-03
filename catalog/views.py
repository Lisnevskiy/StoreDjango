from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Blog


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


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блоги'}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publishing_flag=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'creation_date', 'image')
    success_url = reverse_lazy('catalog:blogs')
    extra_context = {'title': 'Создание блога'}

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Страница блога'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'creation_date', 'image')
    extra_context = {'title': 'Редактирование блога'}

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blogs', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
