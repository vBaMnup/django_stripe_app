from django.db import models


class Item(models.Model):
    """ Модель товара """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
