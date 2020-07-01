from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from .models import Lead


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
    # paginate query results
    all_leads = Lead.objects.all()
    paginator = Paginator(all_leads, 5)  # Show 5 leads per page.
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    context = {
            'all_leads': Lead.objects.all(),
            'page_obj': page_object,
        }

    return render(request, 'query_results.html', context)
