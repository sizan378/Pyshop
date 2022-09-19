from django.contrib import admin
from search.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display= ('title', 'authors', 'average_rating', 'language_code', 'num_pages','ratings_count','text_reviews_count','publication_date')
    search_fields = ['title', 'authors', 'language_code','publication_date', ]
    list_per_page = 25
admin.site.register(Book,BookAdmin)
