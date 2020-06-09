from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

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
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        # if no errors, create new user
        new_user = User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            birthday=request.POST['bday'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        messages.success(request, "Registration successful!")
        print("Created a new user")
        print(request.POST['bday'])
        # redirect to a success route
        return redirect('/success')



    
    # redirect to success page
    return redirect('/success')


def success(request):
    # render success page
    return render(request, 'success.html')

