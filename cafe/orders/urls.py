from django.urls import path
from orders.views import * 

app_name = "orders"

urlpatterns = [
    path("", MainView.as_view(), name="main"),

    # Customers
    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/add/", CustomerCreateView.as_view(), name="add_customer"),
    path("customers/edit/<int:pk>/", CustomerUpdateView.as_view(), name="edit_customer"),
    path("customers/delete/<int:pk>/", CustomerDeleteView.as_view(), name="delete_customer"),

    # Menu Items
    path("menu-items/", MenuItemListView.as_view(), name="menu_list"),
    path("menu-items/add/", MenuItemCreateView.as_view(), name="add_menu_item"),
    path("menu-items/edit/<int:pk>/", MenuItemUpdateView.as_view(), name="edit_menu_item"),
    path("menu-items/delete/<int:pk>/", MenuItemDeleteView.as_view(), name="delete_menu_item"),

    # Orders
    path("orders/", OrderListView.as_view(), name="order_list"),
    path("orders/add/", OrderCreateView.as_view(), name="add_order"),
    path("orders/edit/<int:pk>/", OrderUpdateView.as_view(), name="edit_order"),
    path("orders/delete/<int:pk>/", OrderDeleteView.as_view(), name="delete_order"),

    # Order Items
    path("orders/<int:order_id>/items/", OrderItemListView.as_view(), name="order_item_list"),
    path("orders/<int:order_id>/items/add/", OrderItemCreateView.as_view(), name="add_order_item"),
    path("orders/items/edit/<int:pk>/", OrderItemUpdateView.as_view(), name="edit_order_item"),
    path("orders/items/delete/<int:pk>/", OrderItemDeleteView.as_view(), name="delete_order_item"),
]