from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms



def invoice_list(request):
    invoices = models.Invoice.objects.all()
    return render(request, 'invoice/list.html', {'invoices': invoices})



def invoice_create(request):
    if request.method == 'POST':
        form = forms.InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = forms.InvoiceForm()
    return render(request, 'invoice/form.html', {'form': form})



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



def invoice_detail(request, pk):
    invoice = get_object_or_404(models.Invoice, pk=pk)
    return render(request, 'invoice/detail.html', {'invoice': invoice})