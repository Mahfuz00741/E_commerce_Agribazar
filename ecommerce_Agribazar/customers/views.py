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
        error_message = None
        if not first_name:
            error_message = 'First Name Required.. !!'
        elif len(first_name) < 4:
            error_message = 'First Name must be four character..'
        elif not last_name:
            error_message = 'Last Name Required.. !!'
        elif len(last_name) < 4:
            error_message = 'Last Name must be four character..'
        elif not mobile_number:
            error_message = 'Phone Number Required.. !!'
        elif len(mobile_number) < 11:
            error_message = 'Phone Number at least eleven character..'
        elif not email:
            error_message = 'Email Address Required.. !!'
        elif customer.signup_email_exits():
            error_message = 'Email already registered..'
        elif not address:
            error_message = 'Address Required.. !!'
        elif not password:
            error_message = 'Password Required.. !!'
        elif len(password) < 6:
            error_message = 'Password at least six character long..'

        if not error_message:
            customer.save()
            return redirect('index')

        else:
            dict = {
                'error': error_message
            }
            return render(request, 'customers/signup.html', dict)