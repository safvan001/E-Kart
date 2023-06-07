from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.http import HttpResponse

def searchresult(request):
    products=None
    query=None
    if request.method=="POST":
        query=request.POST.get('q')
        if query:
            products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})

# Create your views here.
