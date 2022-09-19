from search.views import BooksView
from django.urls import path
urlpatterns = [
    path('', BooksView.as_view(), name='book'),
]

