from django.db import models

# Create your models here.


class ItemManager(models.Manager):
    """
    The manager for the item
    """
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    image = models.CharField(max_length=100)
    date = models.DateTimeField('date published')

    objects = ItemManager()
