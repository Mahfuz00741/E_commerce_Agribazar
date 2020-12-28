from django.contrib import admin
from customers.models import Customer, Complain, Subscribe_customer

# Register your models here.
class Admin_display_customer(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'mobile_number']

admin.site.register(Customer, Admin_display_customer)

class Admin_display_complain(admin.ModelAdmin):
    list_display = ['phone_number', 'full_name', 'email', 'message']

admin.site.register(Complain, Admin_display_complain)

class Admin_display_subcribe(admin.ModelAdmin):
    list_display = ['email', 'coupon']

admin.site.register(Subscribe_customer, Admin_display_subcribe)


