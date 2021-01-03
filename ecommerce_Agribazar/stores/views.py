from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from categories.models import Category
from customers.models import Subscribe_customer

# Create your views here.

class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

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
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('index')


class About(View):
    def get(self, request):
        return render(request, 'stores/about.html')


def footer(request):
    categories = Category.objects.all()
    product = None
    category_request = request.GET.get('category')
    if category_request:
        product = Product.all_product_by_categoryId(self, category_request)
    else:
        product = Product.objects.all()
    dict = {
        'product_list': product,
        'category_list': categories
    }
    return render(request, 'partials/_footer.html', dict)

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        product = Product.get_all_product_byid(ids)
        print(product)
        return render(request, 'stores/cart.html', {'products': product})