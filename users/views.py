from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as login_view, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm
from books.models import Book


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_view(request, user)
                if user.is_staff:
                    return redirect('admin_book_list')
                else:
                    return redirect('book_list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_view(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@staff_member_required
def admin_book_list(request):
    return render(request, 'admin/books.html', {'books': Book.objects.all()})

def book_list(request):
    return render(request, 'books.html', {'books': Book.objects.all()})