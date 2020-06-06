from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description

# Create your views here.


def index(request):
    context = {
        'all_courses': Course.objects.all(),
        'descriptions': Description.objects.all()
    }
    return render(request, 'index.html', context)


def add_course(request):
    new_course = Course.objects.create(name=request.POST['name'])
    new_desc = Description.objects.create(
        course=new_course,
        description=request.POST['course_desc'])
    print("Added new course and description entries to db")
    return redirect('home')


def delete_course(request, id):
    context = {
        'this_course': Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)


def process_delete(request, id):
    delete_me = Course.objects.get(id=id)
    delete_me.delete()
    print('Deleted course from the database.')
    return redirect('home')