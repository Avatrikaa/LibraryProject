from django.contrib import admin
from .models import Book, Author, Genre, BookBorrowing


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_authors', 'genre', 'publication_date', 'quantity_in_stock')
    search_fields = ('title', 'authors__name', 'genre__name')
    list_filter = ('genre', 'publication_date')

    def display_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    display_authors.short_description = 'Authors'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(BookBorrowing)
class BookBorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrowed_date', 'returned_date')
    list_filter = ('borrowed_date', 'returned_date')
    search_fields = ('book__title', 'user__email')