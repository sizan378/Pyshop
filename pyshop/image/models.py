from django.db import models

from inventory.models import Inventory


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    Inventory = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    url = models.ImageField(upload_to='image')
    alternative_text = models.CharField(max_length=100)
    is_feature = models.BooleanField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        db_table = 'image'
