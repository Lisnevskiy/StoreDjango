from django import forms

from catalog.models import Product, Version

PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class CleanNameFormMixin:
    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in PROHIBITED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Используется запрещенное слово')

        return cleaned_data


class CleanDescriptionFormMixin:
    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in PROHIBITED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Используется запрещенное слово')

        return cleaned_data


class ProductForm(CleanNameFormMixin, CleanDescriptionFormMixin,forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class ModeratorProductForm(CleanDescriptionFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'publishing_flag')


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control
