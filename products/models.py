from django.db import models
from django.core.validators import URLValidator

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(validators=[URLValidator()])
    #image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.image)