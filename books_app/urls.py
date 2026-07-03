from django.urls import path
from books_app import views

urlpatterns = [
    path('', views.book_list, name='index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('books/admin/', views.get_admin_list, name='admin'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
]
