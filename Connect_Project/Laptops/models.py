from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    processor = models.CharField(max_length=50)
    ram = models.IntegerField()
    ram_type = models.CharField(max_length=256)
    storage = models.IntegerField()
    storage_type = models.CharField(max_length=255)
    gpu = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='laptops/')

    def __str__(self):
        return self.name