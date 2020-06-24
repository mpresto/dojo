from django.shortcuts import render, HttpResponse, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.


def index(request):
    context = {
        'all_notes': Note.objects.all(),
        'noteForm': NoteForm(),
    }
    return render(request, 'notes/index.html', context)


def create_note(request):
    if request.method == 'POST':
        Note.objects.create(content=request.POST['note'])
    context = {
        'all_notes': Note.objects.all(),
    }
    return render(request, 'notes/note_fragment.html', context)
