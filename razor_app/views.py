from django.shortcuts import render
from . models import Donation
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def donate(request):
    if request.method=='POST':
        sender_name=request.POST.get('name')
        sender_email=request.POST.get('email')
        amount1=int(request.POST.get('amount'))*100
        
        client=razorpay.Client(auth=("rzp_test_BfsmPHcf38hNpJ", "iKlgJsHXQmvoRFGuqkHxp0wq"))
        payment=client.order.create({'amount':amount1,'currency':'INR'})
        payment['name']=sender_name
        payment['email']=sender_email
        print(payment)
        donate=Donation(name=sender_name,email=sender_email,amount=amount1,payment_id=payment['id'],paid=False)
        return render(request, 'donate.html',{'payment':payment})
    return render(request, 'donate.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    

@csrf_exempt
def success(request):
    if request.method=='POST':
        return render(request, 'success.html')
    return render(request, 'success.html')    

