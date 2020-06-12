from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def index(request):
    # login / registration page
    # redirect to books/
    return HttpResponse("Login/Reg Page")

def login(request):
    # process login
    pass

def register(request):
    #proces
    pass

def logout(request):
    # logout (clear session) and redirect to login page
    request.session.flush()
    return redirect('/login')