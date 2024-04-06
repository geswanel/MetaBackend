from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=255, default='Fiction')

    def __str__(self) -> str:
        return self.genre

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=1)