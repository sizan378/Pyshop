from django.shortcuts import render
from search.models import Book
from search.serializers import BookSerializers
from rest_framework.generics import ListCreateAPIView


class BooksView(ListCreateAPIView):
    serializer_class = BookSerializers
    queryset = Book.objects.all()