from django.contrib import admin
from .models import Car, Photos, Order


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Photos)
class CarPhotosAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass