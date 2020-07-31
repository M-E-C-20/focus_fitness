# Generated by Django 3.0.8 on 2020-07-31 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20200718_1105'),
        ('profiles', '0004_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='membership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='memberships.UserMembership'),
            preserve_default=False,
        ),
    ]
