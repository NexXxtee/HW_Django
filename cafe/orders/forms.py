from django import forms
from .models import Customer, MenuItem, Order, OrderItem

# Customer Form 
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone_number"]  # Поля, которые будут в форме
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите имя"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите телефон"}),
        }

# MenuItem Form 
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "description", "price", "category", "available"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Название блюда"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Описание блюда", "rows": 3}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Цена"}),
            "category": forms.Select(choices=[("Напитки", "Напитки"), ("Основные блюда", "Основные блюда"), ("Десерты", "Десерты")], attrs={"class": "form-control"}),
            "available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

#  Order Form 
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer", "items", "status"]
        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "items": forms.SelectMultiple(attrs={"class": "form-control"}),
            "status": forms.Select(choices=[("Ожидается", "Ожидается"), ("В процессе", "В процессе"), ("Завершён", "Завершён")], attrs={"class": "form-control"}),
        }

#  OrderItem Form 
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantity"]
        widgets = {
            "menu_item": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Количество"}),
        }
