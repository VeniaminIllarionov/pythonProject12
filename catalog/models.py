from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100),
    description = models.TextField(),

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.description}'


class Product(models.Model):
    name = models.CharField(max_length=100),
    description = models.TextField(),
    image = models.ImageField(upload_to='/templates/'),
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
    created_at = models.DateField(auto_now_add=True),
    updated_at = models.DateField(auto_now=True),

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.category}{self.name} - {self.description}\n{self.created_at}-{self.updated_at}'
