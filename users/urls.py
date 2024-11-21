from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('books/', views.book_list, name='book_list'),
    path('admin/books/', views.admin_book_list, name='admin_book_list'),
]