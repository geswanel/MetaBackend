from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Dish(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

    def __str__(self) -> str:
        return f"{self.title} - {self.description} | {self.price}"
    
    def __repr__(self) -> str:
        return self.title