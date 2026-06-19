from django.urls import path
from books_app import views

urlpatterns = [
    path('', views.book_list, name='index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]
