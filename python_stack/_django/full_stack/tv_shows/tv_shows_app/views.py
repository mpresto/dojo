from django.shortcuts import render, HttpResponse, redirect
from .models import Show


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
    if request.method == "POST":
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['desc']
            )
        print(f'Added {new_show.id} to the database')
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
    if request.method == "POST":
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['desc']
        show_to_update.save()
    return redirect('home')


def delete_show(request, id):
    # delete show from db, redirect home
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('home')