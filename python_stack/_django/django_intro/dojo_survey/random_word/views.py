from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.


def index(request):
    # check counter value
    if 'counter' not in request.session:
        request.session['counter'] = 0  # if none, set counter to 0    
    request.session['counter'] += 1  # increment counter value by 1
    request.session['random_string'] = get_random_string(length=14)  # generate new random_string
    return render(request, 'random_word/index.html')


def reset(request):
    request.session.flush()
    return redirect('/random_word')

