from django.contrib import admin
from stores.models import Product

# Register your models here.
'''class Admin_site_display(admin.ModelAdmin):
    list_display = ['name']'''

admin.site.register(Product)
