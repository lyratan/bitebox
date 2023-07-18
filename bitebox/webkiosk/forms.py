from django.forms import ModelForm #file contains classes that allow us to create forms for website, better to separate file to keep things clean
from .models import Food, Customer, Order

class FoodForm(ModelForm): #inherit from model form
    class Meta: #inner class
        model = Food
        fields = ['name', 'description', 'price'] #three input fields

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'city']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['paymentmode','quantity', 'customer', 'food']
