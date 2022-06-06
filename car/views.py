from django.shortcuts import render
from django.urls import reverse

from .models import Car, Order


def base(request):
    car = Car.objects.get(id=1)
    return render(request, 'base.html', {'car': car})


def cars(request):
    all_cars = Car.objects.all()
    return render(request, 'car/cars.html', {'cars': all_cars})


def car(request, pk):
    one_car = Car.objects.get(id=pk)
    return render(request, 'car/car_details.html', {'car': one_car})


def buy(request, pk):
    one_car = Car.objects.get(id=pk)
    return render(request, 'car/buy.html', {'car': one_car})


def order(request):
    if request.method == 'POST':
        message = 'Thanks for purchase! soon administrators will write/call to You for details'
        customer = request.user
        form = request.POST
        car_n = form.get('car_name')
        car_p = form.get('car_price')
        user_num = form.get('user_number')
        Order.objects.create(customer=customer, mail=customer.email, car=car_n, description=user_num+' '+car_p)
    else:
        return reverse('car:base')
    return render(request, 'car/ordered.html', {'message': message})


def about(request):
    return render(request, 'car/about.html')