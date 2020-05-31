from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


# Create your views here.

def book(request):
    # render book homepage
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'books_index.html', context)


def process_book(request):
    # process create a new book
    if request.method == 'POST':
        new_book = Book.objects.create(
            title=request.POST['book_title'],
            desc=request.POST['book_desc']
            )
        print(new_book.title)
    # redirect to book homepage
    return redirect('/books')


def detail_book(request, id):
    # render book detail page
    exclude_authors = Book.objects.get(id=id).authors.all()

    context = {
        'this_book': Book.objects.get(id=id),
        'these_authors': Book.objects.get(id=id).authors.all(),
        'all_authors': Author.objects.exclude(id__in=exclude_authors),
    }
    return render(request, 'book_detail.html', context)


def add_author(request):
    # add an author to book's authors
    if request.method == "POST":
        added_author = Author.objects.get(id=request.POST['select_author'])
        added_book = Book.objects.get(id=request.POST['book_id'])

        added_author.books.add(added_book)
        print('Author added to book')

    return redirect('/books')


def author(request):
    # render author homepage
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors_index.html', context)


def process_author(request):
    # process create a new author
    if request.method == "POST":
        new_author = Author.objects.create(
            first_name=request.POST['author_fname'],
            last_name=request.POST['author_lname']
            )
        print(new_author.first_name)
    # redirect to author homepage
    return redirect('/authors')


def detail_author(request, id):
    # render author detail page
    exclude_books = Author.objects.get(id=id).books.all()

    context = {
        'this_author': Author.objects.get(id=id),
        'these_books': Author.objects.get(id=id).books.all(),
        'all_books': Book.objects.exclude(id__in=exclude_books),
    }
    return render(request, 'author_detail.html', context)


def add_book(request):
    # add a book to author's books
    if request.method == "POST":
        added_book = Book.objects.get(id=request.POST['select_book'])
        added_author = Author.objects.get(id=request.POST['author_id'])

        added_book.authors.add(added_author)
    return redirect('/authors')