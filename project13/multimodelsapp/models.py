from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(default=10)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField()

    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f"Order #{self.id} for {self.customer.name}"

























