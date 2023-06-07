from django.shortcuts import render
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def allProdCat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,cslug):
    c=Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug) #for particular object use get unless use filter for a group of objects
    return render(request,'products.html',{'p':p,'c':c})

def prodetail(request,pslug):
    p=Product.objects.get(slug=pslug)
    return render(request,'detail.html',{'p':p})
def register(request):
    if(request.method == "POST"):
        u=request.POST['u']
        fs=request.POST['fs']
        ls = request.POST['ls']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if p==cp:
            user=User.objects.create_user(username=u,first_name=fs,last_name=ls,email=e,password=p)
            user.save()
            return allProdCat(request)
        else :
            messages.error(request, 'Passwords do not match')
    return render(request,'register.html')

def user_logout(request):
    logout(request)
    return allProdCat(request)

def user_login(request):
    if (request.method == "POST"):
      u=request.POST['u']
      p=request.POST['p']
      user = authenticate(username=u,password=p)
      if user:
        login(request,user)
        return allProdCat(request)
      else:
         messages.error(request,'password is invalid')

    return render(request,'login.html')