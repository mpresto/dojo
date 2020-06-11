from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Message, Comment
from login_app.models import User


# Create your views here.

def index(request):
    if 'username' not in request.session:
        return redirect('login')
    return render(request, 'wall/index.html')


def post_message(request):
    # get user id from form hidden input and save in sessions
    # process form data and create message in db
    # redirect home
    return redirect('/wall')


def post_comment(request):
    pass


def delete_message(request):
    pass

