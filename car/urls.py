from django.contrib import admin
from django.urls import path
from .views import base, cars, car, buy, order, about

app_name = 'car'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('product-cars/', cars, name='cars'),
    path('product-car-dtl/<int:pk>/', car, name='car_details'),
    path('car-<int:pk>/buy', buy, name='buy'),
    path('car-order/', order, name='order'),
    path('about-us/', about, name='about'),
]

