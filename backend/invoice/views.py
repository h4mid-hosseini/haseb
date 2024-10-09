from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms


@login_required
def invoice_list(request):
    if request.user.is_superuser:
        invoices = models.Invoice.objects.all()
    else:
        invoices = models.Invoice.objects.filter(owner=request.user)

    return render(request, 'invoice/list.html', {'invoices': invoices})



@login_required
def invoice_create(request):
    if request.method == 'POST':
        form = forms.InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = forms.InvoiceForm()
    return render(request, 'invoice/form.html', {'form': form})



@login_required
def invoice_update(request, pk):
    invoice = get_object_or_404(models.Invoice, pk=pk)
    if request.method == 'POST':
        form = forms.InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = forms.InvoiceForm(instance=invoice)
    return render(request, 'invoice/form.html', {'form': form})



def invoice_detail(request, invoice_code):
    invoice = get_object_or_404(models.Invoice, unique_code=invoice_code)
    tax_rate = invoice.owner.tax_rate
    total_invoice_price = int(sum([item.total() for item in invoice.items.all()]))
    print(total_invoice_price)
    tax_fee = int(total_invoice_price * (tax_rate / 100))
    total_with_tax = int(total_invoice_price + total_invoice_price * (tax_rate / 100))


    return render(request, 'invoice/detail.html', {'invoice': invoice, 'total_invoice_price':total_invoice_price, 'tax_rate':tax_rate, 'tax_fee':tax_fee, 'total_with_tax':total_with_tax})