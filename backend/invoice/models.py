from django.db import models
from django.contrib.auth import get_user_model
import string
import random

User = get_user_model()


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    


class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', related_name='items', on_delete=models.CASCADE)  # ForeignKey to Invoice
    title = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def total(self):
        return self.price * self.quantity



class Invoice(models.Model):

    def random_unique_code():
        return f''.join(random.choices(string.ascii_uppercase + string.digits, k=45))
    

    unique_code = models.CharField(max_length=45, unique=True, default=random_unique_code)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

