from django.shortcuts import render
from search.models import Book
from search.serializers import BookSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from search.pagination import CustomNumberPagination


class BooksListCreateView(ListCreateAPIView):
    serializer_class = BookSerializers
    pagination_class = CustomNumberPagination
    
    queryset = Book.objects.all()

class BookRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = BookSerializers
    queryset = Book.objects.all()