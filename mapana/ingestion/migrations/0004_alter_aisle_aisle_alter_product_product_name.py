# Generated by Django 4.2.19 on 2025-02-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingestion', '0003_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aisle',
            name='aisle',
            field=models.CharField(max_length=50, verbose_name='aisle'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=150, verbose_name='product_name'),
        ),
    ]
