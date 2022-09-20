from django.shortcuts import render
from search.models import Book
from search.serializers import BookSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from search.pagination import CustomNumberPagination
from rest_framework import filters

class BooksListCreateView(ListCreateAPIView):

    # Setting the serializer class to the BookSerializers class and the queryset to the Book model.
    serializer_class = BookSerializers
    queryset = Book.objects.all()

    # Filtering the data based on the search field.
    search_fields = ['authors']
    filter_backends = (filters.SearchFilter,)

    # Setting the pagination class to the custom pagination class that we created.
    pagination_class = CustomNumberPagination
    

class BookRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = BookSerializers
    queryset = Book.objects.all()