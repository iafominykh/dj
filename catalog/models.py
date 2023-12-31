from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


NULLABLE = {'null': True, 'blank': True}
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    specification = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'



    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    specification = models.TextField(**NULLABLE,verbose_name='Описание')
    preview_image = models.ImageField(**NULLABLE, upload_to='product/', verbose_name='Изображение')
    category = models.ForeignKey(Category, **NULLABLE, on_delete=models.CASCADE, verbose_name="категория")
    price = models.IntegerField(**NULLABLE, verbose_name='Цена')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,**NULLABLE, verbose_name='Покупатель')


    def __str__(self):
        return f'{self.title} ({self.category}): {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Version(models.Model):
    version_number = models.IntegerField(verbose_name='номер версии')
    version_title = models.CharField(max_length=150, verbose_name='название версии')
    sign_current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.version_title}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'



