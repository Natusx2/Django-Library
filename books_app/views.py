from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from books_app.forms import book
from books_app.models import Book


def book_list(request):
    books = Book.objects.all()
    selected_genre = request.GET.get('genre', '')
    genre_values = [value for value, name in Book.GENRE_CHOICES]

    if selected_genre in genre_values:
        books = books.filter(genre=selected_genre)

    return render(request, 'books/book_list.html', {
        'books': books,
        'featured_books': Book.objects.all()[:3],
        'genres': Book.GENRE_CHOICES,
        'selected_genre': selected_genre,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def get_admin_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_admin.html', {'books': books})


def delete_book(request, book_id):
    item = get_object_or_404(Book, id=book_id)
    item.delete()
    messages.warning(request, 'Book was deleted')
    return redirect('/books/admin/')


def create_book(request):
    if request.method == 'POST':
        form = book.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book was created')
            return redirect('/books/admin/')
        else:
            messages.error(request, 'Please check the form')
            return render(request, 'books/create.html', {'form': form})

    form = book.BookForm()
    return render(request, 'books/create.html', {'form': form})


def edit_book(request, book_id):
    item = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = book.BookForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, 'Book was updated')
            return redirect('/books/admin/')
        else:
            messages.error(request, 'Please check the form')
            return render(request, 'books/edit.html', {'form': form})

    form = book.BookForm(instance=item)
    return render(request, 'books/edit.html', {'form': form})


def about(request):
    return render(request, 'books/about.html')
