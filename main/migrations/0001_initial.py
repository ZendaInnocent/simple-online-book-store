# Generated by Django 3.0.4 on 2020-03-18 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('in_stock', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(to='main.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
        ),
    ]
