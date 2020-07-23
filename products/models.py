from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    amount = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return self.title