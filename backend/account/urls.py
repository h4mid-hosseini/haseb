
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json

MERCHANT = '051bebf3-817f-4d2d-9588-2286396c05db'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"

email = 'info.husseini@gmail.com'  # Optional
mobile = '09023234719'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://haseb.falconhub.ir/account/orders/verify/'
amount=0
o_id=0



def send_request(request, order_id, price):
    global amount, o_id
    amount = price
    o_id = order_id
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": 'توسعه وب حمید حسینی',
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")



def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100 or t_status == -9 or t_status == '-9':
                order= Orders.objects.get(id=o_id)
                order.is_paid=True
                order.save()
                messages.success (request, f"تراکنش موفقیت آمیز بود. کد پیگیری: {str(req.json()['data']['ref_id'])}", 'success')
                return redirect('courses:list')

            elif t_status == 101:
                messages.success (request, f"تراکنش ثبت شد: {req.json()['data']['message']}", 'success')
                return redirect('courses:list')

            else:
                messages.success (request, " تراکنش با شکست مواجه شد.", 'danger')
                return redirect('courses:list')
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        messages.success (request, "تراکنش نا معتبر یا لغو شده توسط کاربر", 'danger')
        return redirect('courses:list')