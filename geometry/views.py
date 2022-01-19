from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.

def rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника шириной {width} и длинной {height} равна - {width * height}.")


def square_area(request, width: int):
    return HttpResponse(f"Площадь квадрата со стороной {width} равна - {width * width}.")


def circle_area(request, radius: int):
    return HttpResponse(f"Площадь круга радиусом {radius} равна - {pi * radius * radius}")


# Первый способ (Минус - нужно указывать точный путь(url).)
#
# def get_rectangle_area(request, width: int, height: int):
#     return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


# Второй способ (Используется функция reverse, она перенаправляет на имя(name=) заданное в urlpatterns.)
def get_rectangle_area(request, width: int, height: int):
    redirect_url_rectangle = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirect_url_rectangle)


def get_square_area(request, width: int):
    redirect_url_square = reverse('square-name', args=[width])
    return HttpResponseRedirect(redirect_url_square)


def get_circle_area(request, radius: int):
    redirect_url_circle = reverse('circle-name', args=[radius])
    return HttpResponseRedirect(redirect_url_circle)
