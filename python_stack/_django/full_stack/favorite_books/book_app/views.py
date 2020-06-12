from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("Books homepage")


def add_book(request):
    # create a book
    pass


def book_detail(request, id):
    # render update form if logged_user = creator
    # or render detail page
    pass


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



