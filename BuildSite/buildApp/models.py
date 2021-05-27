from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
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
    Service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE, related_name="service")
    Datetime = models.DateTimeField(verbose_name="Время оформления заявки")
    Status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.CASCADE)
    DatetimeEnd = models.DateTimeField(verbose_name="Время окончания", null=True, blank=True)
    User = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Service), str(self.Datetime)
