from django.db import models
from django.contrib.auth.models import User


class Provider(User):
    name = models.CharField(max_length=255, default='', verbose_name='Имя')
    phone = models.CharField(max_length=255, default='', verbose_name='Номер телефона')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'


class Consumer(User):
    name = models.CharField(max_length=255, default='', verbose_name='Имя')
    phone = models.CharField(max_length=255, default='', verbose_name='Номер телефона')
    address = models.TextField(default='', verbose_name='Адрес')
    geo_location = models.CharField(max_length=255, default='', verbose_name='Геолокация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'


class Category(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class Product(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='Имя')
    image = models.ImageField(upload_to='product', default='', verbose_name='Картинка', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Store(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


class Order(models.Model):
    STATUS = (
        ('new', 'new_order'),
        ('pending', 'pending_order'),
        ('finished', 'finished_order')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=20, default="new", choices=STATUS)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0, verbose_name='Вес')

    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
