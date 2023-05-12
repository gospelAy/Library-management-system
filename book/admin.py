from django.contrib import admin
from .models import Author, Book


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['email']
    list_per_page = 10


class BookAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'author', 'price']
    list_per_page = 30
    list_filter = ['genre']
# admin.site.register(Author)
# admin.site.register(Book)
