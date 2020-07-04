from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Lead
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def index(request):
    all_leads = Lead.objects.all()
    paginator = Paginator(all_leads, 5)  # Show 5 leads per page.
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    context = {
            'all_leads': Lead.objects.all(),
            'page_obj': page_object,
        }
    return render(request, 'index.html', context)


def paginate(request, id):
    # paginate all leads
    all_leads = Lead.objects.all()
    paginator = Paginator(all_leads, 5)  # Show 5 leads per page.
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    context = {
            'all_leads': Lead.objects.all(),
            'page_obj': page_object,
        }
    return render(request, 'snippets/query_results.html', context)


@csrf_exempt
def search(request):
    # apply filter
    userinput = request.GET['first']
    result = Lead.objects.filter(first_name__icontains=userinput)
    if result:
        messages.success(request, "Your search returned the following:")
    else:
        messages.error(request, "There are no matching leads.")

    # paginate results
    paginator = Paginator(result, 5)  # Show 5 leads per page.
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
            'result': result,
            'page_obj': page_object,
        }
    return render(request, 'snippets/query_results.html', context)
