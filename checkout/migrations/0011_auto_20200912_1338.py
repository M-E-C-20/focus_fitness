# Generated by Django 3.0.8 on 2020-09-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20200910_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
    ]