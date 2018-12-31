from django.shortcuts import render
from django.views.generic import ListView,DetailView
from book.models import Publisher,Book

class PublisherList(ListView):
    model = Publisher


class BookList(ListView):
    model = Book
    context_object_name = 'book_list'


class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = 'publisher'



# Create your views here.
