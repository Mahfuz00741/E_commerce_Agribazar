from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from categories.models import Category
from customers.models import Subscribe_customer

# Create your views here.

class Index(View):
    def get(self, request):
        categories = Category.objects.all()

        product = None
        category_request = request.GET.get('category')
        if category_request:
            product = Product.all_product_by_categoryId(self, category_request)
        else:
            product = Product.objects.all()

        dict = {
            'category_list': categories,
            'product_list': product
        }
        return render(request, 'stores/index.html', dict)

    def post(self, request):
        email = request.POST.get('Email')
        subscribe = Subscribe_customer(
            email=email
        )
        subscribe.save()
        return redirect('index')


class About(View):
    def get(self, request):
        return render(request, 'stores/about.html')