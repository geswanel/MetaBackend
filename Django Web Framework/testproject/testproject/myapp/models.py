from django.db import models

# Create your models here.

class Dish(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.title} - {self.description} | {self.price}"
    
    def __repr__(self) -> str:
        return self.title