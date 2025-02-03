from django import forms
from .models import Customer, MenuItem, Order, OrderItem


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone_number"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите имя"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите телефон"}),
        }


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "description", "price", "category", "available"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Название блюда"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Описание блюда", "rows": 3}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Цена"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class OrderForm(forms.ModelForm):
    menu_items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.filter(available=True),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    quantities = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите количество через запятую (например, 2, 1, 3)"}),
        required=True
    )

    class Meta:
        model = Order
        fields = ["customer", "status"]
        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        order = super().save(commit=False)
        order.save()  # Сохраняем сам заказ, чтобы у него появился ID

        # Очищаем старые позиции
        order.items.clear()

        # Получаем выбранные блюда и введенные количества
        menu_items = self.cleaned_data["menu_items"]
        quantities = self.cleaned_data["quantities"].split(",")

        # Проверяем корректность данных
        if len(quantities) != len(menu_items):
            raise forms.ValidationError("Количество введенных значений не соответствует числу выбранных блюд.")

        # Создаем OrderItem для каждого блюда
        total_price = 0
        for menu_item, quantity in zip(menu_items, quantities):
            quantity = int(quantity.strip())
            if quantity < 1:
                continue
            order_item = OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
            total_price += menu_item.price * quantity

        # Обновляем сумму заказа
        order.total_price = total_price
        order.save()

        return order


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantity"]
        widgets = {
            "menu_item": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Количество"}),
        }

    def save(self, commit=True):
        order_item = super().save(commit=False)
        order_item.save()
        order_item.order.calculate_total_price()
        return order_item
