from django.contrib import admin
from . import models


class InvoiceItemInline(admin.TabularInline):
    model = models.InvoiceItem
    min_num = 1 
    can_delete = True
    fields = ('title', 'price', 'quantity')



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'email', 'owner')



@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('unique_code', 'owner', 'customer')
    inlines = [InvoiceItemInline]



@admin.register(models.InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'title', 'price', 'quantity')
