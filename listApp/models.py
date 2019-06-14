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
    photo = models.ImageField(upload_to='uploads', default='')
    date = models.DateTimeField(auto_now_add=True)

    objects = ItemManager()
