from django.contrib import admin

from .models import Category, Service, Status, Orders


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameService', 'Slug', 'Description', 'Specification', 'Category', 'IMG')
    list_display_links = ('id', 'NameService')
    search_fields = ('NameService', 'Description', 'Category')
    prepopulated_fields = {"Slug": ("NameService",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'CategoryName')
    list_display_links = ('id', 'CategoryName')
    search_fields = ('CategoryName',)
    prepopulated_fields = {"Slug": ("CategoryName",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Status)
admin.site.register(Orders)
# Register your models here.
