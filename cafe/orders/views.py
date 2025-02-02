from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, MenuItem, Order, OrderItem
from .forms import CustomerForm, MenuItemForm, OrderForm, OrderItemForm


def main(request):
    return render(request, 'orders/index.html')
# Customers 

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders:customer_list")
    else:
        form = CustomerForm()
    return render(request, "orders/customer_form.html", {"form": form})

def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("orders:customer_list")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "orders/customer_form.html", {"form": form})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect("orders:customer_list")


# Menu Items 

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, "orders/menu_list.html", {"menu_items": menu_items})

def add_menu_item(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders:menu_list")
    else:
        form = MenuItemForm()
    return render(request, "orders/menu_form.html", {"form": form})

def edit_menu_item(request, id):
    menu_item = get_object_or_404(MenuItem, id=id)
    if request.method == "POST":
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect("orders:menu_list")
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, "orders/menu_form.html", {"form": form})

def delete_menu_item(request, id):
    menu_item = get_object_or_404(MenuItem, id=id)
    menu_item.delete()
    return redirect("orders:menu_list")


# Orders

def order_list(request):
    orders = Order.objects.all()
    return render(request, "orders/order_list.html", {"orders": orders})

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("orders:order_list")
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})

def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orders:order_list")
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/order_form.html", {"form": form})

def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect("orders:order_list")


# Order Items 

def order_item_list(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()
    return render(request, "orders/order_item_list.html", {"order": order, "items": items})

def add_order_item(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()
            return redirect("orders:order_item_list", order_id=order.id)
    else:
        form = OrderItemForm()
    return render(request, "orders/order_item_form.html", {"form": form})

def edit_order_item(request, id):
    order_item = get_object_or_404(OrderItem, id=id)
    if request.method == "POST":
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect("orders:order_item_list", order_id=order_item.order.id)
    else:
        form = OrderItemForm(instance=order_item)
    return render(request, "orders/order_item_form.html", {"form": form})

def delete_order_item(request, id):
    order_item = get_object_or_404(OrderItem, id=id)
    order_id = order_item.order.id
    order_item.delete()
    return redirect("orders:order_item_list", order_id=order_id)