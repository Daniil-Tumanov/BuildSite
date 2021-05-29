from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
from django.utils import timezone


class Category(models.Model):
    CategoryName = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.CategoryName

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.id})


class Status(models.Model):
    StatusName = models.CharField(max_length=150)

    def __str__(self):
        return self.StatusName


class Service(models.Model):
    NameService = models.CharField(max_length=150, verbose_name="Наименование услуги")
    Slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    Description = models.TextField(verbose_name="Описание", blank=True)
    Specification = models.TextField(verbose_name="Характеристики", blank=True)
    Category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="category")
    IMG = models.ImageField(upload_to='img/', verbose_name="Изображение")

    def __str__(self):
        return self.NameService

    def get_absolute_url(self):
        return reverse('serviceID', kwargs={'service_slug': self.Slug})


class Orders(models.Model):
    Service = models.ForeignKey(Service, verbose_name="Услуга", null=True, blank=True, on_delete=models.CASCADE, related_name="service")
    Datetime = models.DateTimeField(default=timezone.now, verbose_name="Время оформления заявки")
    Status = models.ForeignKey(Status, default="1", verbose_name="Статус", on_delete=models.CASCADE)
    DatetimeEnd = models.DateTimeField(verbose_name="Время окончания", null=True, blank=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE)
    Comment = models.TextField(verbose_name="Комментарий к заказу", null=True, blank=True)
    Phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return str(self.Service)

    def get_absolute_url(self):
        return reverse('makeOrder', kwargs={'service_id': self.id})
