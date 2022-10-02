from django.db import models

class Attribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'attribute'
        verbose_name_plural = 'attributes'
        db_table = 'attribute'
