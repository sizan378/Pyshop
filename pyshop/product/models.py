from django.db import models

from category.models import Category


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    slug = models.SlugField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'product'
