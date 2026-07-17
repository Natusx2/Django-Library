from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from books_app.forms import book
from books_app.forms import comment
from books_app.models import Book


def get_favorite_ids(request):
    return request.session.get('favorite_books', [])


def book_list(request):
    books = Book.objects.all()
    selected_genre = request.GET.get('genre', '')
    genre_values = [value for value, name in Book.GENRE_CHOICES]
    favorite_ids = get_favorite_ids(request)

    if selected_genre in genre_values:
        books = books.filter(genre=selected_genre)

    return render(request, 'books/book_list.html', {
        'books': books,
        'featured_books': Book.objects.all()[:3],
        'genres': Book.GENRE_CHOICES,
        'selected_genre': selected_genre,
        'favorite_ids': favorite_ids,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comments.all().order_by('-created_at')
    favorite_ids = get_favorite_ids(request)

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': comments,
        'comment_form': comment.CommentForm(),
        'is_favorite': book.id in favorite_ids,
    })


def add_comment(request, book_id):
    item = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = comment.CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.book = item
            new_comment.save()
            messages.success(request, 'Comment was added')
            return redirect(f'/books/{book_id}/')
        else:
            messages.error(request, 'Please check your comment')

    return redirect(f'/books/{book_id}/')


def favorite_list(request):
    favorite_ids = get_favorite_ids(request)
    books = Book.objects.filter(id__in=favorite_ids)
    return render(request, 'books/favorites.html', {
        'books': books,
        'favorite_ids': favorite_ids,
    })


def add_to_favorites(request, book_id):
    item = get_object_or_404(Book, id=book_id)
    favorite_ids = get_favorite_ids(request)

    if item.id not in favorite_ids:
        favorite_ids.append(item.id)
        request.session['favorite_books'] = favorite_ids
        messages.success(request, 'Book was added to favorites')
    else:
        messages.info(request, 'Book is already in favorites')

    return redirect(request.META.get('HTTP_REFERER', '/favorites/'))


def remove_from_favorites(request, book_id):
    item = get_object_or_404(Book, id=book_id)
    favorite_ids = get_favorite_ids(request)

    if item.id in favorite_ids:
        favorite_ids.remove(item.id)
        request.session['favorite_books'] = favorite_ids
        messages.warning(request, 'Book was removed from favorites')

    return redirect(request.META.get('HTTP_REFERER', '/favorites/'))


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
