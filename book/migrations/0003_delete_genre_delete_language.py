# Generated by Django 4.2.1 on 2023-05-12 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_summary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]