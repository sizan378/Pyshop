
from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'
        db_table = 'category'
