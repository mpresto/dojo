from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def process(request):
    if request.method == 'POST':  
        context = { 
            "name": request.POST['name'],
            "location": request.POST['location'],
            "language": request.POST['language'],
            "comments": request.POST['comments'],
            }
        return render(request, 'results.html', context)
    return render(request, 'results.html')
