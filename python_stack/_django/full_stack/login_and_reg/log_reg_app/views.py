from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.


def index(request):
    # render login and registration forms
    return render(request, 'index.html')


def login(request):
    # validate login
    # include hashing
    # redirect to success page
    return redirect('/success')


def register(request):
    # validate registration form info
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:  # if no errors, create new user
        # hash password:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)

        new_user = User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            birthday=request.POST['bday'],
            email=request.POST['email'],
            password=pw_hash
        )
        messages.success(request, "Registration successful!")
        print("Created a new user")
        print(request.POST['bday'])
        request.session['username'] = new_user.first_name
        # redirect to a success route
        return redirect('/success')


def success(request):
    # render success page
    context = {
    }
    return render(request, 'success.html', context)

