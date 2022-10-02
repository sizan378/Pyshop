from tabnanny import verbose
from django.db import models

from inventory.models import Inventory


class StockControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    Inventory = models.OneToOneField(Inventory, on_delete=models.DO_NOTHING)
    unit = models.IntegerField()
    last_checked = models.DateTimeField()


    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = 'stock'
        verbose_name_plural = 'stocks'
        db_table = 'stock'
