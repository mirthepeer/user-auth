from django.contrib import admin
from .models import Book, Author, Genre, BookInstance, Language

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(BookInstance)