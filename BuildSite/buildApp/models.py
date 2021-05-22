from django.db import models


# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName


class Status(models.Model):
    StatusName = models.CharField(max_length=150)

    def __str__(self):
        return self.StatusName


class Service(models.Model):
    NameService = models.CharField(max_length=150, verbose_name="Наименование услуги")
    Description = models.TextField(verbose_name="Описание", null=True)
    Specification = models.TextField(verbose_name="Характеристики", null=True)
    Category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="category")
    IMG = models.ImageField(upload_to='img/', verbose_name="Изображение")

    def __str__(self):
        return self.NameService


class Orders(models.Model):
    Service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE, related_name="service")
    Datetime = models.DateTimeField(verbose_name="Время оформления заявки")
    Status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.CASCADE)
    DatetimeEnd = models.DateTimeField(verbose_name="Время окончания", null=True)

    def __str__(self):
        return self.Datetime

