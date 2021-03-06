# Generated by Django 3.0.8 on 2020-07-17 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('memberships', '0002_auto_20200717_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('allowed_memberships', models.ManyToManyField(to='memberships.Membership')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('video_url', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('Program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.Program')),
            ],
        ),
    ]
