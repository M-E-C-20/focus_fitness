# Generated by Django 3.0.8 on 2020-08-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20200804_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_receipt',
            field=models.CharField(default='', max_length=254),
        ),
    ]
