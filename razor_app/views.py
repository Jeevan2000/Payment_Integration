from django.shortcuts import render
from . models import Donation
import razorpay
from Payment_Gateway.settings import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
import math
from django.db.models import Sum
from django.template.loader import render_to_string
# Create your views here. 

client=razorpay.Client(auth=(KEY_ID, SECRET_KEY))

def home(request):
    result = Donation.objects.all().filter(paid=True).aggregate(Sum('amount')) #in dict format "{'amount__sum': 10100}"
    collection = int(result.get('amount__sum')/100)
    
    return render(request, 'home.html',{'collection':collection})

def donate(request):
    if request.method=='POST':
        sender_name=request.POST.get('name')
        sender_email=request.POST.get('email')
        amount1=int(request.POST['amount'])
        amount1 = math.floor(amount1 * 100)
        client=razorpay.Client(auth=(KEY_ID, SECRET_KEY))
        payment=client.order.create({'amount':amount1,'currency':'INR'})
        payment['name']=sender_name
        payment['email']=sender_email
        payment['keyid']=KEY_ID
       # print(payment)
        
        donate=Donation(name=sender_name,email=sender_email,amount=amount1,paymentid=payment['id'],paid=False)
        donate.save()
        return render(request, 'donate.html',{'payment':payment})
    return render(request, 'donate.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    

@csrf_exempt
def success(request):
    if request.method=='POST':
        data=request.POST
        print(data)
        order_id=data['razorpay_order_id']
        payment_id=data['razorpay_payment_id']
        user=Donation.objects.get(paymentid=order_id)
        user.paid=True
        
        user.save()
        user=Donation.objects.get(paymentid=order_id)
        print(user.email,user.name,payment_id)
        #total_coll+=(int(user.amount)//100)
        details=dict()
        details['name']=user.name
        details['amount']=int(user.amount)//100
        details['paymentid']=payment_id
        msg_txt= render_to_string('email.txt')
        msg_html=render_to_string('newemail.html',{'details':details})
        send_mail("Sparks Foundation : Your Donation was Successful", msg_txt, settings.EMAIL_HOST_USER, [user.email],html_message=msg_html)
        return render(request, 'success.html')
       
       

