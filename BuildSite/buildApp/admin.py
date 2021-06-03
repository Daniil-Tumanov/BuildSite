from django.contrib import admin

from .models import Category, Service, Status, Orders, Feedback


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


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'StatusName')
    list_display_links = ('id', 'StatusName')
    search_fields = ('StatusName',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'TextFeedback', 'User')
    list_display_links = ('id', 'TextFeedback', 'User')
    search_fields = ('TextFeedback',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Service', 'Datetime', 'DateEnd', 'Status', 'Phone', 'Comment')
    list_display_links = ('id', 'User', 'Service', 'Datetime', 'Status', 'Phone', 'Comment')
    search_fields = ('User',)

admin.site.site_title = "ООО «Промтехсервис»"
admin.site.site_header = "Администрирование ООО «Промтехсервис»"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
