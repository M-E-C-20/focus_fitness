# Generated by Django 3.0.8 on 2020-07-16 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('membership', models.CharField(choices=[('Free', 'free'), ('Professional', 'pro')], default='Free', max_length=30)),
                ('price', models.IntegerField(default=20)),
                ('stripe_plan_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(max_length=50)),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='memberships.Membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('user_memdership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberships.UserMembership')),
            ],
        ),
    ]
