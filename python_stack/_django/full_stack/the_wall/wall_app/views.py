from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Message, Comment
from login_app.models import User


# Create your views here.

def index(request):
    if 'user_id' not in request.session:  # send back to login
        return redirect('/login')
    context = {
        'all_messages': Message.objects.all()
    }
    return render(request, 'wall/index.html', context)


def post_message(request):
    # get user id from form hidden input and save in sessions
    logged_user = User.objects.get(id=request.session['user_id'])
    new_message = Message.objects.create(user=logged_user, content=request.POST['content'])
    # process form data and create message in db
    # redirect home
    return redirect('/wall')


def post_comment(request):
    pass


def delete_message(request):
    pass

