from django.db import models


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=155, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("YORUBA", "Y"),
        ('ENGLISH', "E"),
        ('IBO', "I"),
        ('ENGLISH', "E"),
    ]
    GENRE_CHOICE = [
        ('FICTION', "FIC"),
        ('POLITICS', "POL"),
        ('FINANCE', "FIN"),
        ('ROMANCE', "ROM"),
    ]
    tittle = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICE)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.tittle} {self.author} {self.author}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('RETURNED', 'R'),
        ('BORROWED', 'B')
    ]
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=55)
    borrower = ""
