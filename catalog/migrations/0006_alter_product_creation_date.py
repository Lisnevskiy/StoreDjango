# Generated by Django 4.2.3 on 2023-08-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_creation_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="creation_date",
            field=models.DateField(auto_now_add=True, verbose_name="Дата создания"),
        ),
    ]
