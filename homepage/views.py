from django.shortcuts import render
from .models import stock
from django.core.paginator import Paginator
from django.views.generic import ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homepage(request):
    stock_list = stock.objects.exclude(rank=int(0)).order_by('-rank')
    page = request.GET.get('page', 1)
    paginator = Paginator(stock_list, 40)
    try:
        stocks = paginator.page(page)
    except PageNotAnInteger:
        stocks = paginator.page(1)
    except EmptyPage:
        stocks = paginator.page(paginator.num_pages)
    is_paginated = paginator.count
    page_obj = paginator.get_page(page)
    return(render(request, 'homepage.html', { 'stocks': stocks , 'is_paginated': is_paginated, 'page_obj':page_obj}))


# Create your views here.
#
# def homepage(requests):
#     stocks = Stock.objects.all()
#     paginator = Paginator(stocks, 4) # Show 25 contacts per page.
#     page = requests.GET.get('page', 1)
#     print(page)
#     try:
#         page_number = paginator.page(page)
#     except PageNotAnInteger:
#         page_number = paginator.page(1)
#     except EmptyPage:
#         page_number = paginator.page(paginator.num_pages)
#     page_number = requests.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#     'stocks':stocks,
#     'page_obj':page_obj
#     }
#     return(render(requests, 'homepage.html', context = context))

# def homepage(request):
#     stock_list = Stock.objects.all()
#     paginator = Paginator(stock_list, 4) # Show 25 contacts per page.
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     print(page_obj)
#     return render(request, 'homepage.html', {'page_obj': page_obj})

# class homepage(ListView):
#     model = Stock
#     template_name = 'homepage.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'stocks'  # Default: object_list
#     paginate_by = 4
#     queryset = Stock.objects.all()  # Default: Model.objects.all()
