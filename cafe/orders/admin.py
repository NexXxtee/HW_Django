from django.contrib import admin
from .models import Customer, Order, OrderItem, MenuItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "created_at")
    list_filter = ("created_at", "email", "phone_number", "name")
    search_fields = ("name", "email", "phone_number")

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available")
    list_filter = ("category", "available", "name")
    search_fields = ("name",)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("menu_item", "order", "quantity")
    list_filter = ("quantity",)
    search_fields = ("menu_item__name",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price", "status", "created_at")
    list_filter = ("created_at", "status")
    search_fields = ("customer__name",)