from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateField()
    number_of_pages = models.PositiveIntegerField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    GENDER_CHOICES = [
        ("M", 'Male'),
        ("F", 'Female'),
        ("O", 'Other')
    ]

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender  = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    def __str__(self) -> str:
        return self.name


class Ownership(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name