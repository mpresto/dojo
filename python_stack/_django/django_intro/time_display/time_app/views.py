from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.


def index(request):
    context = {
        'time': strftime("%b %d, %Y \n%I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

# Oct 26, 2013
# 11:26 AM