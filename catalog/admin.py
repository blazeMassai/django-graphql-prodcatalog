from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    search_fields = ('name',)



@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'quantity', 'category',)
    search_fields = ('name', )