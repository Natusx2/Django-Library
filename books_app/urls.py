from django.urls import path
from books_app import views

urlpatterns = [
    path('', views.book_list, name='index'),
    path('books/admin/', views.book_admin, name='book_admin'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]
