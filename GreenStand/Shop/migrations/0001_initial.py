# Generated by Django 2.2.1 on 2019-06-03 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('producer', models.CharField(max_length=100)),
                ('producer_certification_number', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit_quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
