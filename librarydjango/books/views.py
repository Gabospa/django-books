""" Books Views """

# Django
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect


# Model
from .models import Book

# Utilities
from .services import get_books, get_book

def add(request):
    
    title = request.POST.get('book_title')
    author = request.POST.get('book_author')
    category = request.POST.get('book_categories')
    description = request.POST.get('book_description')
    image = request.POST.get('book_image')

    book = Book(
        title = title,
        author = author,
        category = category,
        description = description,
        image = image,
    )

    book.save()

    return render (request, 'books/addDetail.html', {
        'book': book
    })

def go_back(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class BookListView(ListView):
    """ List of saved books """
    template_name = "books/listBook.html"
    queryset = Book.objects.all().order_by('-id')


class BookDetailView(DetailView):
    """ Detail of saved books by slug """
    model = Book
    template_name = 'books/detailOwnBook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SearchApiView(TemplateView):
    """ Request list of book from API, using query """

    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = get_books(self.query())
        print(self.query())
        return context

    def query(self):
        if self.request.GET.get('q') == None:
            return 'books'
        return self.request.GET.get('q')
        

class DetailApiView(TemplateView):
    """ Detail of single book from API """

    model = Book
    template_name = 'books/detailBook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = get_book(context['arg1'])
        return context

    