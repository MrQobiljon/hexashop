from django.db import models

# Create your models here.


class Product(models.Model):
    choice = (
        ('mens', "Men's"),
        ('womens', "Women's"),
        ('kids', "Kid's"),
        ('accessories', "Accessories")
    )
    category = models.CharField(max_length=15, choices=choice)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField(default=0)
