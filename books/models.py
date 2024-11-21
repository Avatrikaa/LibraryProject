from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(_('name'), max_length=200)
    biography = models.TextField(_('biography'), blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_('title'), max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')
    publication_date = models.DateField(_('publication date'))
    quantity_in_stock = models.PositiveIntegerField(_('quantity in stock'), default=0)

    def __str__(self):
        return self.title


class BookBorrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowings')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='book_borrowings')
    borrowed_date = models.DateTimeField(_('borrowed date'), default=timezone.now)
    returned_date = models.DateTimeField(_('returned date'), null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.user.email}"