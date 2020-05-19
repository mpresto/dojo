from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")


def create(request):
    return HttpResponse("Placeholder for the create blog page")


def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}")


def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")


def destroy(request, number):
    return HttpResponse(f"Here's where we'd delete blog {number}")