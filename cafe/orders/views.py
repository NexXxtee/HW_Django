from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Customer, MenuItem, Order, OrderItem
from .forms import CustomerForm, MenuItemForm, OrderForm, OrderItemForm

# Главная страница
class MainView(TemplateView):
    template_name = "orders/index.html"

# Customers
class CustomerListView(ListView):
    model = Customer
    template_name = "orders/customer_list.html"
    context_object_name = "customers"

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "orders/customer_form.html"
    success_url = reverse_lazy("orders:customer_list")

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "orders/customer_form.html"
    success_url = reverse_lazy("orders:customer_list")

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "orders/customer_confirm_delete.html"
    success_url = reverse_lazy("orders:customer_list")

# Menu Items
class MenuItemListView(ListView):
    model = MenuItem
    template_name = "orders/menu_list.html"
    context_object_name = "menu_items"

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "orders/menu_form.html"
    success_url = reverse_lazy("orders:menu_list")

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "orders/menu_form.html"
    success_url = reverse_lazy("orders:menu_list")

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "orders/menu_confirm_delete.html"
    success_url = reverse_lazy("orders:menu_list")

# Orders
class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:order_list")

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:order_list")

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders/order_confirm_delete.html"
    success_url = reverse_lazy("orders:order_list")

# Order Items
class OrderItemListView(ListView):
    model = OrderItem
    template_name = "orders/order_item_list.html"
    context_object_name = "items"

    def get_queryset(self):
        order = get_object_or_404(Order, id=self.kwargs["order_id"])
        return order.items.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = get_object_or_404(Order, id=self.kwargs["order_id"])
        return context

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "orders/order_item_form.html"
    
    def form_valid(self, form):
        order = get_object_or_404(Order, id=self.kwargs["order_id"])
        order_item = form.save(commit=False)
        order_item.order = order
        order_item.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("orders:order_item_list", kwargs={"order_id": self.kwargs["order_id"]})

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "orders/order_item_form.html"
    
    def get_success_url(self):
        return reverse_lazy("orders:order_item_list", kwargs={"order_id": self.object.order.id})

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = "orders/order_item_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("orders:order_item_list", kwargs={"order_id": self.object.order.id})