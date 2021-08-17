from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import *
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
# Create your views here.

def home(request):
    orders = Order.objects.all()#butun orderleri getiririk
    customer = Customer.objects.all()#butun customerleri getiririk
    total_customer = customer.count()#butun customerlerin sayini getirirk
    totat_orders = orders.count()#butun orderlerin sayini getiririk
    delivered = orders.filter(status='Delivered').count()#orderleri statusu delivered olanlarin sayini getirir
    pending = orders.filter(status='Pending').count()#orderlerin icinde statusu pending olanlarin sayini getirir
    context = {
        'orders' : orders ,
        'customer' : customer ,
        'total_customer':total_customer,
        'totat_orders': totat_orders,
        'delivered':delivered,
        'pending':pending,
    }#'key':word
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()#butun productlari gosterir
    return render(request,'accounts/products.html',{'products':products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)#customerleri id-e gore getirir
    orders = customer.order_set.all()#orderde customer ordere baglanib deye order_set var dir verende
    order_count = orders.count()#orderlerin sayini
    myFilter = OrderFilter(request.GET, queryset = orders )
    orders = myFilter.qs

    context = {
        'customer':customer,
        'orders':orders,
        'order_count':order_count,
        'myFilter':myFilter,
    }
    return render(request,'accounts/customer.html',context)

def create_order(request,pk):#pk=primary key
    OrderFormSet = inlineformset_factory(Customer , Order , fields=('product','status'), extra=10)#Ordere esasen Customer-leri getrecek ve elave 10 sahe
    customer = Customer.objects.get(id=pk)#customerleri id-e gore getirir
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)#ici bos olan formlari getrecek
    # form = OrderForm(initial={'customer':customer})#formu cagirirq
    if request.method == 'POST':
        # print(request.POST)
        # form = OrderForm(request.POST)#formu requestden gelen dataynan doldur
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'form' : formset,
    }

    return render(request,'accounts/order_form.html',context)



def update_order(request,pk):
    order = Order.objects.get(id=pk)#orderleri id-e gore getiririk sebeb id-e gore update elyirik
    form = OrderForm(instance=order)#formu order classina  gore doldurq
    if request.method == 'POST':
        # print(request.POST)
        form = OrderForm(request.POST,instance=order)#Formu request-in datasina gore gonderirik
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form,
    }
    return render(request,'accounts/order_form.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)#id-ne gore silirik
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item':order,#key htmldi word orderdi
    }
    return render(request,'accounts/delete.html',context)