from django.db import models

# Create your models here.
# CUSTOMER MODEL
class Customer(models.Model): 
    firstname= models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
 
    def get_customer_initials(self):
        return self.firstname[0] + self.lastname[0]

    def __str__(self):
        return f'''CUSTOMER #{self.id} 
NAME: {self.firstname} {self.lastname}
ADDRESS: {self.address}
CITY: {self.city}'''

# FOOD MODEL
class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_food_shortname(self):
        return self.name[0:3]

    def __str__(self):
        return f''' FOOD #{self.id}
NAME: {self.name}
DESCRIPTION: {self.description}
PRICE: {self.price}'''
    
#ORDER MODEL
class Order(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('CH', 'Cash'), #tupple values are fixed
        ('CD', 'Card'),
        ('DW', 'Digital Wallet'), #dont forget comma
    ]

    orderdatetime = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(max_length=2, choices = PAYMENT_MODE_CHOICES) #dw digital wallet, cd card (CH, CD, DW)
    quantity = models.IntegerField() #quantity of 5 burgers
    food = models.ForeignKey(Food, on_delete=models.CASCADE) #food being ordered - needs FK to reference from other table. 'Food' model represents our food records. models.CASCADE means baby order itself will be deleted itself if Hamburger Parent order is deleted. if models.PROTECT, hamburgers cannot be deleted since parents cannot leave orphans. models.SET_NULL is delete hambruger but orders will remain as NULL. But you need to set the whole line as nullable
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__ (self): #For line 45, cant be self.name as self refers to order itself but we wanna get the name of food. so we wanna get self as order with food attribute
        return f'''ORDER# {self.id}
CUSTOMER NAME: {self.customer.firstname} {self.customer.lastname}
FOOD NAME: {self.food.name} 
FOOD QUANTITY: {self.quantity}
PAYMENT MODE: {self.get_paymentmode_display()}
ORDER DATE AND TIME: {self.orderdatetime}'''