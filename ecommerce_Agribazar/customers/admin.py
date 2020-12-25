from django.contrib import admin
from customers.models import Customer

# Register your models here.
class Admin_display(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'mobile_number']

admin.site.register(Customer, Admin_display)


