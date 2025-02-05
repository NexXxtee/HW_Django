from django.urls import path
from orders import views

app_name = "orders"

urlpatterns = [ 
    path('', views.main, name='main'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/edit/<int:id>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:id>/', views.delete_customer, name='delete_customer'),
    path('menu-items/', views.menu_list, name='menu_list'),
    path('menu-items/add/', views.add_menu_item, name='add_menu_item'),
    path('menu-items/edit/<int:id>/', views.edit_menu_item, name='edit_menu_item'),
    path('menu-items/delete/<int:id>/', views.delete_menu_item, name='delete_menu_item'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/edit/<int:id>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:id>/', views.delete_order, name='delete_order'),
]