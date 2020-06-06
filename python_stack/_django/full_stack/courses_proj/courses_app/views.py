from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description, Comment
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, 'index.html', context)


def add_course(request):
    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('home')
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


def comments(request, id):
    context = {
        'this_course': Course.objects.get(id=id),
    }
    return render(request, 'comments.html', context)


def add_comment(request, id):
    this_course = Course.objects.get(id=id)
    new_comment = Comment.objects.create(
        course=this_course,
        comment=request.POST['content'])
    print("Added new comment to db")
    return redirect(f'/comments/{id}')