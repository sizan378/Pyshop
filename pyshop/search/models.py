from django.db import models
from django.utils.translation import gettext as _

class Book(models.Model):
    title = models.CharField(_('title'), max_length=1000, null=False, db_index=True)
    authors = models.CharField(_('authors'), max_length=1000)
    average_rating = models.CharField(_('average_rating'), max_length=1000)
    isbn = models.CharField(_('isbn'), max_length=100)
    isbn13 = models.CharField(_('isbn13'), max_length=100)
    language_code = models.CharField(_('language_code'), max_length=1000)
    num_pages = models.CharField(_('num_pages'), max_length=1000)
    ratings_count = models.CharField(_('ratings_count'), max_length=1000)
    text_reviews_count = models.CharField(_('text_reviews_count'), max_length=1000)
    publication_date = models.DateField()
    publisher = models.CharField(_('publisher'), max_length=1000)


    def __str__(self):
        return self.title, self.authors, self.publication_date, self.ratings_count, self.publisher,