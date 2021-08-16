from django.http import HttpResponse
from django.shortcuts import render
from.models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    totat_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders' : orders ,
        'customers' : customers ,
        'total_customers':total_customers,
        'totat_orders': totat_orders,
        'delivered':delivered,
        'pending':pending,
    }#'key':word
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'order_count':order_count,
    }
    return render(request,'accounts/customer.html',context)