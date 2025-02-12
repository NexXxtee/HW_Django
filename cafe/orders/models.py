from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя клиента")
    email = models.EmailField(max_length=100, verbose_name="Email клиента")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон клиента")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("Напитки", "Напитки"),
        ("Основные блюда", "Основные блюда"),
        ("Десерты", "Десерты"),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория"
    )
    available = models.BooleanField(default=True, verbose_name="Доступно")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"


class Order(models.Model):
    STATUS_CHOICES = [
        ("Ожидается", "Ожидается"),
        ("В процессе", "В процессе"),
        ("Завершён", "Завершён"),
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Клиент"
    )
    items = models.ManyToManyField(
        MenuItem, through="OrderItem", verbose_name="Пункты меню"
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Общая сумма"
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Ожидается",
        verbose_name="Статус",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def calculate_total_price(self):
        self.total_price = sum(
            item.menu_item.price * item.quantity for item in self.orderitem_set.all()
        )
        self.save()

    def __str__(self):
        return f"Заказ #{self.id} - {self.customer.name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, verbose_name="Пункт меню"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"
