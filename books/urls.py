from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.regular_book_list, name='book-list'),
    path('admin/books/', views.admin_book_list, name='admin-book-list'),
    path('admin/books/add/', views.add_book, name='add-book'),
    path('admin/books/<int:pk>/edit/', views.admin_edit_book, name='edit-book'),
    path('admin/books/<int:pk>/delete/', views.admin_delete_book, name='delete-book'),
]
