from django.contrib import admin
from . import models

# Define the inline for InvoiceItem
class InvoiceItemInline(admin.TabularInline):
    model = models.InvoiceItem  # The related model (InvoiceItem)
    extra = 1  # How many empty rows to show for creating new items
    min_num = 1  # Minimum number of invoice items
    can_delete = True  # Allow deletion of invoice items
    fields = ('title', 'price', 'quantity')  # Fields to display

# Admin for Customer
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'email', 'owner')

# Admin for Invoice with inline InvoiceItem
@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('unique_code', 'owner', 'customer')
    inlines = [InvoiceItemInline]  # Add the InvoiceItemInline to InvoiceAdmin

# Admin for InvoiceItem (optional, in case you still want a separate admin view for invoice items)
@admin.register(models.InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'title', 'price', 'quantity')
