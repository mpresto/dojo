from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import views
from .models import Book
from login_app.models import User


# Create your views here.

def index(request):
    if 'user_id' not in request.session:  # send back to login
        return redirect('/login')
    context = {
        'all_books': Book.objects.all(),
        'logged_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'book/index.html', context)


def add_book(request):
    # check for errors:
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        # create a book instance:
        logged_user = User.objects.get(id=request.session['user_id'])
        new_book = Book.objects.create(
            uploaded_by=logged_user,
            title=request.POST['title'],
            desc=request.POST['desc'],
        )
        print("Created new book.")
        # add to user's favorites:
        new_book.liked_by.add(logged_user)
    # redirect to homepage
    return redirect(f'/books/{new_book.id}')


def book_detail(request, id):
    # render update form if logged_user = creator
    # or render detail page
    return HttpResponse('book detail page.')


def update_book(request):
    # process update form data
    # redirect to ? home?
    pass


def add_favorite(request):
    # create new favorite relationship
    pass


def remove_favorite(request):
    # remove favorite relationship
    pass


def user_detail(request, id):
    # render user detail page
    pass



