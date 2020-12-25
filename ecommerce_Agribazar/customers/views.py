from django.shortcuts import render, redirect
from django.views import View
from .models import Customer

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'customers/login.html')

class Signup(View):
    def get(self, request):
        return render(request, 'customers/signup.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            email=email,
            address=address,
            password=password
        )
        customer.save()
        return redirect('index')
        #error_message = None