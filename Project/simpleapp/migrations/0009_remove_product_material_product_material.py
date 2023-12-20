# Generated by Django 4.2.7 on 2023-12-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0008_product_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='material',
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ManyToManyField(through='simpleapp.ProductMaterial', to='simpleapp.material'),
        ),
    ]