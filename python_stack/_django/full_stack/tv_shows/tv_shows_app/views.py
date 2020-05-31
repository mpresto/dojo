from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def index(request):
    return redirect('home')


def shows_index(request):
    return HttpResponse('Shows homepage and directory')


def add_show(request):
    return HttpResponse('a page to add a show')


def process_show(request):
    return HttpResponse('POST data, redirect to show detail page')


def show_detail(request):
    return HttpResponse('a page for show details')


def edit_show(request):
    return HttpResonse('render template for editing show info')


def update_show(request):
    return HttpResponse('POST updates, reidrect home')


def delete_show(request):
    return HttpResponse('POST deletion, redirect home')