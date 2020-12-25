from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'customers/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.login_email_exits(email)

        error_message = None
        if customer:
            password_check = check_password(password, customer.password)
            if password_check:
                request.session['customer_id'] = customer.id
                return redirect('index')
            else:
                error_message = 'Email or Password Incorrect.. !!'
                return render(request, 'customers/login.html')

        else:
            error_message = 'Email or Password Incorrect.. !!'
            return render(request, 'customers/login.html', {'error': error_message})




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
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('index')

        else:
            value = {
                'first_name': first_name,
                'last_name': last_name,
                'mobile_number': mobile_number,
                'email': email,
                'address': address,
            }
            dict = {
                'values': value,
                'error': error_message
            }
            return render(request, 'customers/signup.html', dict)

class logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('login')

    def post(self, request):
        return render(request, 'pages/index.html')

class contact(View):
    def get(self, request):
        return render(request, 'customers/contact.html')