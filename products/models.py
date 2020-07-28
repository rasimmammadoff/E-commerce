from django.db import models

# product model
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    amount = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=4)
    minSize = models.IntegerField(default=21)
    maxSize = models.IntegerField(default=26)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Products'

    def __str__(self):
        return self.title

# category model
class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title


