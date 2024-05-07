from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименованик'),
    description = models.TextField(verbose_name='Описание'),

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.description}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование'),
    description = models.TextField(verbose_name='Описание'),
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', null=True, blank=True),
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания'),
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения'),

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.category}{self.name} - {self.description}\n{self.created_at}-{self.updated_at}'
