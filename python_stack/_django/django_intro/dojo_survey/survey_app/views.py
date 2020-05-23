from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    return render(request, '/survey/index.html')


def process(request):
    # capture POST data and redirect to /results
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    
    return redirect('/survey/results')


def results(request):
    # got here from /process 
    # render data captured from POST
    context = { 
            "name": request.session['name'],
            "location": request.session['location'],
            "language": request.session['language'],
            "comments": request.session['comments'],
            }
    return render(request, "survey/results.html", context)
