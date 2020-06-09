from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    # render login and registration forms
    return render(request, 'index.html')


def login(request):
    # validate login form
    # include hashing
    # redirect to success page
    return redirect('/success')


def register(request):
    # validate registration form info
    # create new user
    # redirect to success page
    return redirect('/success')


def success(request):
    # render success page
    return render(request, 'success.html')

