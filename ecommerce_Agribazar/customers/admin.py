from django.contrib import admin
from customers.models import Customer, Complain

# Register your models here.
class Admin_display_customer(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'mobile_number']

admin.site.register(Customer, Admin_display_customer)

class Admin_display_complain(admin.ModelAdmin):
    list_display = ['phone_number', 'full_name', 'email', 'message']

admin.site.register(Complain, Admin_display_complain)


