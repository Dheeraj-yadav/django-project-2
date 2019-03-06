from django.shortcuts import render
from django.http import HttpResponse
from .models import product

def index(request):
    return render(request,
                  'homepage.html',
                  )

def page(request):
    products = product.objects.all()
    return render(request, 'page.html', {'products': products})


