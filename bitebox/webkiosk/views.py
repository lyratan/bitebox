from django.contrib import messages #to allow for popups if you edited or added
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Food, Customer, Order
from .forms import FoodForm, CustomerForm, OrderForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate as django_authenticate, login as django_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):  
    return render(request,'webkiosk/welcome.html')

def testview(request):
    return render(request, 'webkiosk/testpage.html')

def listfood(request):
    fl = Food.objects.all()
    context = {'foodlist': fl} #key is food list, value is fl. context gets passed to food_list.html
    return render(request, 'webkiosk/food_list.html', context) #passes the context object to the food_list.html

def createfood(request):
    if request.method == 'GET': #visitng localhost
        f = FoodForm() #instance for foodform
    elif request.method == 'POST': #submitting something
        f = FoodForm(request.POST) #contains all data that user typed in
        if f.is_valid():
            f.save()
            return redirect('webkiosk:food-list') #webkiosk is app name so we add app name on urls.py

    context = { 'form': f, 'formheading': 'Add Food'}#pass to template through context
    return render(request, 'webkiosk/food_form.html', context)

def detailfood(request, pk): #the pk in 'food/<int:pk>/' in urls.py refers to the pk in this line
    f = Food.objects.get(id=pk) #get food record with id as pk
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

def updatefood(request, pk): #update food record
    food = Food.objects.get(id=pk) #get food record before update
    if request.method == 'GET':
        form = FoodForm(instance=food) #create food form but it cant be empty since we want to get the food deets. This gets requets of the food displayed so its not empty 
    elif request.method == 'POST': #this is for when you change the deets
        form = FoodForm(request.POST, instance=food) #it gets whatever you type new in the field
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updates.') #create message after food is saved
    context = {'form': form, 'formheading': 'Update Food'} #form goes to key form
    return render(request, 'webkiosk/food_form.html',context)

def deletefood(request, pk): #looks for object, delete it, then redirect to food-list
    f = Food.objects.get(id=pk)
    if request.method == 'GET':
        context = {'food': f} #create context, pass food record that we get from f
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
        f.delete()
        return redirect('webkiosk:food-list')

#added Customers here
def listcustomer(request):
    cl = Customer.objects.all()
    context = {'customerlist': cl} #key is food list, value is fl. context gets passed to food_list.html
    return render(request, 'webkiosk/customer_list.html', context) #passes the context object to the food_list.html

def createcustomer(request):
    if request.method == 'GET': #visitng localhost
        c = CustomerForm() #instance for foodform
    elif request.method == 'POST': #submitting something
        c = CustomerForm(request.POST) #contains all data that user typed in
        if c.is_valid():
            c.save()
            return redirect('webkiosk:customer-list') #webkiosk is app name so we add app name on urls.py

    context = { 'form': c, 'formheading': 'Add Customer'}#pass to template through context
    return render(request, 'webkiosk/food_form.html', context)

def detailcustomer(request, pk): #the pk in 'customer/<int:pk>/' in urls.py refers to the pk in this line
    c = Customer.objects.get(id=pk) #get customer record with id as pk
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def updatecustomer(request, pk): #update food record
    customer = Customer.objects.get(id=pk) #get food record before update
    if request.method == 'GET':
        form = CustomerForm(instance=customer) #create food form but it cant be empty since we want to get the food deets. This gets requets of the food displayed so its not empty 
    elif request.method == 'POST': #this is for when you change the deets
        form = CustomerForm(request.POST, instance=customer) #it gets whatever you type new in the field
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record successfully updates.') #create message after food is saved
    context = {'form': form, 'formheading': 'Update Customer'} #form goes to key form
    return render(request, 'webkiosk/customer_form.html',context)

def deletecustomer(request, pk): #looks for object, delete it, then redirect to food-list
    c = Customer.objects.get(id=pk)
    if request.method == 'GET':
        context = {'customer': c} #create context, pass food record that we get from f
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method == 'POST':
        c.delete()
        return redirect('webkiosk:customer-list')
    
#added Orders here
def orderlist(request):
    ol = Order.objects.all()
    context = {'orderlist': ol} #key is food list, value is fl. context gets passed to food_list.html
    return render(request, 'webkiosk/order_list.html', context) #passes the context object to the food_list.html

def createorder(request):
    if request.method == 'GET': #visitng localhost
        o = OrderForm() #instance for foodform
    elif request.method == 'POST': #submitting something
        o = OrderForm(request.POST) #contains all data that user typed in
        if o.is_valid():
            o.save()
            return redirect('webkiosk:order-list')
        return render(request, 'webkiosk/order_form.html', context)
    
    context = { 'form': o, 'formheading': 'Add Order'}#pass to template through context
    return render(request, 'webkiosk/order_form.html', context)
        
def detailorder(request, pk): #the pk in 'customer/<int:pk>/' in urls.py refers to the pk in this line
    o = Order.objects.get(id=pk) #get customer record with id as pk
    context = {'order': o}
    return render(request, 'webkiosk/order_detail.html', context)

def deleteorder (request, pk):
    o = Order.objects.get(id=pk)
    if request.method == "GET":
        context = {'order': o}
        return render (request, 'webkiosk/order_delete.html', context)
    elif request.method == "POST":
        o.delete()
        return redirect ('webkiosk:order-list')
    
def updateorder(request, pk): #update food record
    order = Order.objects.get(id=pk) #get food record before update
    if request.method == 'GET':
        form = OrderForm(instance=order) #create food form but it cant be empty since we want to get the food deets. This gets requets of the food displayed so its not empty 
    elif request.method == 'POST': #this is for when you change the deets
        form = OrderForm(request.POST, instance=order) #it gets whatever you type new in the field
        if form.is_valid():
            form.save()
            messages.success(request, 'Order record successfully updates.') #create message after food is saved
    context = {'form': form, 'formheading': 'Update Order'} #form goes to key form
    return render(request, 'webkiosk/order_form.html',context)

#login
def login_page(request):
    if request.method == 'GET':
        return render(request, 'webkiosk/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webkiosk:food-list')
        else:
            return render(request, 'webkiosk/login.html', {'error': 'Invalid credentials'})