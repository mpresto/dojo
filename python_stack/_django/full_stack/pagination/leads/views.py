from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from .models import Lead


# Create your views here.


# def index(request):
#     context = {
#         'all_leads': Lead.objects.all()
#     }
#     return render(request, 'index.html', context)


def index(request):
    # paginate query results
    all_leads = Lead.objects.all()
    paginator = Paginator(all_leads, 3)  # Show 3 leads per page.
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    context = {
            'all_leads': Lead.objects.all(),
            'page_obj': page_object,
        }

    return render(request, 'index.html', context)
