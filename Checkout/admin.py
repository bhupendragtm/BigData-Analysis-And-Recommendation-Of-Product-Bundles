from django.contrib import admin
from .models import Order,Product

# Register your models here.
#admin.site.register(Order)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","name", "email", "address","city","province","zipcode","date")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","order_id","product_D","total")