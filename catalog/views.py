from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Товары'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Страница товара'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': 'Добавление товара'}

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.owner = self.request.user
            self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users:login'
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Редактирование товара'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        print(formset)
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:products', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users:login'
    model = Product
    success_url = reverse_lazy('catalog:products')
    extra_context = {'title': 'Удаление товара'}


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
