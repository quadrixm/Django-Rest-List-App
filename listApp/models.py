from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='uploads', default='')
    date = models.DateTimeField(auto_now_add=True)
