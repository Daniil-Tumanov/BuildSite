from django.contrib import admin

from .models import Category, Service, Status, Orders

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Status)
admin.site.register(Orders)
# Register your models here.

