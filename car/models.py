from django.db import models
from django.urls import reverse


class Car(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now=True)
    authors = models.TextField()
    in_stock = models.BooleanField(default=True)

    def absolute_url(self):
        return reverse('car:car_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Photos(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='car_photos')

    def __str__(self):
        return self.car.name


class Order(models.Model):
    customer = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    car = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer