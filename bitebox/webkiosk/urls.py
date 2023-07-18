from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'webkiosk'

urlpatterns = [
    # http://localhost.8000/webkiosk/
    path('', views.index, name='index'),
    path('testview/', views.testview, name ='testview'),

    # http://localhost.8000/webkiosk/menu/
    path('menu/', views.listfood, name='food-list'), #calls listfood in views.py file

    #http://localhost:8000/webkiosk/food/new/
    path('food/new/', views.createfood, name='food-create'), #add new food record

    #http://localhost:8000/webkiosk/food/1/
    path('food/<int:pk>/', views.detailfood, name = 'food-detail'), 
         # < int: pk > parameter is an integer with variable name pk. Here, pk = 1, 2, 3, 4 etc..

    ##http://localhost:8000/webkiosk/food/1/edit/
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),

    #http://localhost:8000/webkiosk/food/1/delete
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),

       # http://localhost.8000/webkiosk/customer/
    path('customers/', views.listcustomer, name='customer-list'), #calls listcustomer in views.py file

     #http://localhost:8000/webkiosk/customer/1/
    path('customers/<int:pk>/', views.detailcustomer, name = 'customer-detail'), 
         # < int: pk > parameter is an integer with variable name pk. Here, pk = 1, 2, 3, 4 etc..

    #http://localhost:8000/webkiosk/customer/1/delete
    path('customers/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),

    #http://localhost:8000/webkiosk/customer/new/
    path('customers/new/', views.createcustomer, name='customer-create'), #add new food record

    #http://localhost:8000/webkiosk/food/1/edit/
    path('customers/<int:pk>/edit/', views.updatecustomer, name='customer-update'),

    #http://localhost.8000/webkiosk/order/
    path('order/', views.orderlist, name='order-list'), #calls listcustomer in views.py file

 #http://localhost:8000/webkiosk/order/1/
    path('order/<int:pk>/', views.detailorder, name = 'order-detail'), 
         # < int: pk > parameter is an integer with variable name pk. Here, pk = 1, 2, 3, 4 etc..

# http://localhost:8000/webkiosk/customer/1/delete
    path('order/<int:pk>/delete', views.deleteorder, name="order-delete"),

#http://localhost:8000/webkiosk/customer/new/
    path('order/new/', views.createorder, name='order-create'),

#http://localhost:8000/webkiosk/food/1/edit/
    path('order/<int:pk>/edit/', views.updateorder, name='order-update'),

# http://localhost:8000/webkiosk/login/
    path('login/', views.login_page, name="login"),

    path('logout/', auth_views.LogoutView.as_view(next_page='webkiosk:login'), name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)