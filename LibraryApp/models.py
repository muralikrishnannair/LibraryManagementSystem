from django.db import models

# Create your models here.


class BookDb(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.PositiveIntegerField(default=1)
    is_available=models.BooleanField(default=True)
    published_date=models.DateField(null=True, blank=True)