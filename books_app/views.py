from django.shortcuts import get_object_or_404, redirect, render

from books_app.models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def book_admin(request):
    books = Book.objects.all()
    return render(request, 'books/book_admin.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            cover_url=request.POST.get('cover_url'),
            description=request.POST.get('description'),
            publication_year=request.POST.get('publication_year'),
            genre=request.POST.get('genre'),
            available_copies=request.POST.get('available_copies'),
        )
        return redirect('book_admin')

    return render(request, 'books/book_form.html', {
        'title': 'Create Book',
        'button_text': 'Create',
        'genres': Book.GENRE_CHOICES,
    })


def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.cover_url = request.POST.get('cover_url')
        book.description = request.POST.get('description')
        book.publication_year = request.POST.get('publication_year')
        book.genre = request.POST.get('genre')
        book.available_copies = request.POST.get('available_copies')
        book.save()
        return redirect('book_admin')

    return render(request, 'books/book_form.html', {
        'title': 'Edit Book',
        'button_text': 'Save',
        'book': book,
        'genres': Book.GENRE_CHOICES,
    })


def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_admin')

    return render(request, 'books/book_delete.html', {'book': book})


def about(request):
    return render(request, 'books/about.html')
