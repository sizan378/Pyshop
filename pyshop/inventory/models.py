import uuid

from django.db import models

from product.models import Product
from attribute_value.models import AttributeValue


class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    sku = models.UUIDField(default = uuid.uuid4,
         editable = False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    attribute_value = models.ManyToManyField(AttributeValue)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField()
    is_default = models.BooleanField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = 'inventory'
        verbose_name_plural = 'inventorys'
        db_table = 'inventory'
