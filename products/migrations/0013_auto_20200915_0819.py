# Generated by Django 3.0.8 on 2020-09-15 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200824_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='display_items',
            new_name='sales_items',
        ),
    ]