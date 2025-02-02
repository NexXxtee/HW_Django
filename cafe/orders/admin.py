from django.contrib import admin
from .models import Customer, Order, OrderItem, MenuItem


admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
