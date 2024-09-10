from django.db import models
from django.contrib.auth import get_user_model
import string
import random
from django.utils import timezone


User = get_user_model()


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', related_name='items', on_delete=models.CASCADE)  # ForeignKey to Invoice
    title = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title

    def total(self):
        return self.price * self.quantity



class Invoice(models.Model):

    def random_unique_code():
        return f''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    
    LANGUAGES = [
        ('fa', 'fa'),
        ('en', 'en')
    ]

    CURRENCIES = [
        ('irr', 'ریال'),
        ('usd', '$')
    ]
    unique_code = models.CharField(max_length=45, unique=True, default=random_unique_code)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_deadline = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(choices=CURRENCIES, default=CURRENCIES[0], max_length=20)
    language = models.CharField(choices=LANGUAGES, default=LANGUAGES[0], max_length=20)

    def __str__(self):
        return f'{self.unique_code}'