from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)
    isbn = models.CharField(max_length=11)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    language = models.ForeignKey('Language', on_delete=models.PROTECT)


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()


class Language(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=55)


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('RETURNED', 'R'),
        ('BORROWED', 'B')
    ]
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=55)
    borrower = ""
