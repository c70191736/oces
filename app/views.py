from django.shortcuts import render

from django.conf import settings 
from django.conf.urls.static import static

from .models import Product

from django.views.generic import (ListView, DetailView)


from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')

def product(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'product.html', context)

class ProductListView(ListView): 
    model = Product 
    template_name = 'product.html'
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 12 

class ProductDetailView(DetailView):
    model = Product

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        title = Product.objects.filter(title__contains = search)
        amount = Product.objects.filter(amount__contains = search)
        return render(request, 'search.html', {'search': search, 'title': title, 'amount': amount})
    else:
        return render(request, 'search.html')