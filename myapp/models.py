from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.author}"
