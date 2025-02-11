# Generated by Django 5.1.5 on 2025-02-02 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя клиента')),
                ('email', models.EmailField(max_length=100, verbose_name='Email клиента')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Телефон клиента')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('category', models.CharField(choices=[('Напитки', 'Напитки'), ('Основные блюда', 'Основные блюда'), ('Десерты', 'Десерты')], max_length=50, verbose_name='Категория')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая сумма')),
                ('status', models.CharField(choices=[('Ожидается', 'Ожидается'), ('В процессе', 'В процессе'), ('Завершён', 'Завершён')], default='Expected', max_length=50, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.menuitem', verbose_name='Пункт меню')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Элемент заказа',
                'verbose_name_plural': 'Элементы заказа',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='orders.OrderItem', to='orders.menuitem', verbose_name='Пункты меню'),
        ),
    ]
