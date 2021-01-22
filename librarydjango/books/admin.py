""" Books Admin """

# Django
from django.contrib import admin

# Models
from .models import Book

class BookAdmin(admin.ModelAdmin):
    """ Model for book admin """
    fields = ('title', 'description', 'author', 'category', 'image')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Book, BookAdmin)