from search.views import BooksListCreateView, BookRetrieveUpdateView
from django.urls import path
urlpatterns = [
    path('', BooksListCreateView.as_view(), name='book_create'),
    path('<int:pk>/', BookRetrieveUpdateView.as_view(), name='book_update'),
]

