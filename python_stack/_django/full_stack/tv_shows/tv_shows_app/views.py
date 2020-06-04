from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show, ShowManager


# Create your views here.


def index(request):
    # redirect rool url to /shows
    return redirect('home')


def shows_index(request):
    # render homepage with table displaying all shows
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'show_index.html', context)


def add_show(request):
    # render form to add new show to db
    return render(request, 'add_show.html')


def process_show(request):
    # from /create, POST form data to db and redirect to show detail page
    errors = Show.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('add_new')
    else:
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['desc']
            )
        print(f'Added {new_show.id} to the database')
        messages.success(request, "Successfully added new show!")
    return redirect('home')


def show_detail(request, id):
    # render show detail page
    context = {
        'this_show': Show.objects.get(id=id),
    }
    return render(request, 'show_detail.html', context)


def edit_show(request, id):
    # render edit show form
    context = {
        'this_show': Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)


def update_show(request, id):
    # process edit form data, update db, redirect home
    show_to_update = Show.objects.get(id=id)
    errors = Show.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('edit', id=id) # with no named routes, try: {id}/edit
    else:
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['desc']
        show_to_update.save()
        print(f'Updated {show_to_update.id} in the database')
        messages.success(request, "Successfully updated show!")
    return redirect('home')


def delete_show(request, id):
    # delete show from db, redirect home
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('home')