from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product-detail', kwargs={'pk': self.pk})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='product-thumbnails/', null=True)
    image = models.ImageField(upload_to='product-images/')


class ProductTag(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

