from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Book, Author, Genre
from .forms import BookForm

def regular_book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

@staff_member_required
def admin_book_list(request):
    books = Book.objects.all()
    return render(request, 'admin/books.html', {'books': books})



@staff_member_required
def admin_edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin-book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'admin/edit_book.html', {'form': form, 'book': book})

@staff_member_required
def admin_delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('admin-book-list')

@staff_member_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        authors_input = request.POST.get('authors')
        genre_input = request.POST.get('genre')
        publication_date = request.POST.get('publication_date')
        quantity_in_stock = request.POST.get('quantity_in_stock')

        authors = []
        for author_name in [a.strip() for a in authors_input.split(',')]:
            author, _ = Author.objects.get_or_create(name=author_name)
            authors.append(author)

        genre, _ = Genre.objects.get_or_create(name=genre_input)

        book = Book.objects.create(
            title=title,
            genre=genre,
            publication_date=publication_date,
            quantity_in_stock=quantity_in_stock
        )
        book.authors.set(authors)
        book.save()

        return redirect('admin-book-list')

    return render(request, 'admin/add_book.html')