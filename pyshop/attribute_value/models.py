from django.db import models

from attribute.models import Attribute

class AttributeValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'attribute-value'
        verbose_name_plural = 'attribute-values'
        db_table = 'attribute-value'
