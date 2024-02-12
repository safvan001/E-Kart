from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart
from cart.models import Account,Orders
# import razorpay

from django.http import HttpResponse
@login_required
def cart_view(request):
    total=0
    try:
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total +=i.quantity*i.products.price
    except Cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart,'total':total})



@login_required
def add_to_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity += 1
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(products=product,user=user,quantity=1)
        cart.save()
    return redirect('cart:cart_view')
@login_required
def decreaser(request,p):
    user=request.user
    product = Product.objects.get(id=p)
    try:
        cartitem=Cart.objects.get(products=product,user=user)
        if cartitem.quantity>1:
            cartitem.quantity -=1
            cartitem.save()
        else:
            cartitem.delete()

    except:
        pass
    return redirect('cart:cart_view')
@login_required
def delete(request,p):
    product = Product.objects.get(id=p)
    user=request.user
    try:
        cart_item=Cart.objects.get(products=product,user=user)
        cart_item.delete()
    except:
        pass
    return redirect('cart:cart_view')
# @login_required
# def order(request):
#     total=0
#     items=0
#     msg=0
#     if (request.method == "POST"):
#         ad=request.POST['ad']
#         ph=request.POST['ph']
#         ac=request.POST['ac']
#         user=request.user
#         cart=Cart.objects.filter(user=user)
#         for i in cart:
#             total+=i.quantity*i.products.price
#             items+=i.quantity
#             a=Account.objects.get(acctnumber=ac)
#             if float(a.amount) >=total:
#                 a.amount=a.amount-total
#                 a.save()
#                 for i in cart:
#                     o=Orders.objects.create(user=user,products=i.products,address=ad,phone=ph,order_status="paid",noofitems=i.quantity)
#                     o.save()
#                 cart.delete()
#                 msg="Order placed succesfully!!!"
#                 return render(request,'orderdetail.html',{'msg':msg,'total':total,'items':items})
#             else:
#                 msg="insufficient Amount.You cant place order!!"
#                 return render(request,'orderdetail',{'msg':msg})
#     return render(request,'form.html')
from django.conf import settings
import razorpay
# @login_required
# def order(request):
#     total = 0
#     items = 0
#     msg = 0
#
#     try:
#         user = request.user
#         cart = Cart.objects.filter(user=user)
#         for i in cart:
#             total += i.quantity * i.products.price
#             items += i.quantity
#     except Cart.DoesNotExist:
#         pass
#
#     client = razorpay.Client(auth=(settings.RAZOR_PAY_KEY_ID))
#
#     # Create a Razorpay order
#     order_amount = int(total * 100)  # Razorpay amount is in paisa
#     order_currency = 'INR'
#     order_receipt = 'order_rcptid_11'
#     payment = client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt)
#
#     msg = "Order placed successfully!!!"
#     return render(request, 'orderdetail.html', {'msg': msg, 'payment': payment, 'items': items})



@login_required
def u_r_orders(request):
    user= request.user
    o= Orders.objects.filter(user=user,order_status="paid")

    return render(request,'your orders.html',{'o':o,'name':user})