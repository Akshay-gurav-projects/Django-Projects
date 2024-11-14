from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.author_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()

