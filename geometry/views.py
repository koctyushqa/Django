from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi


# Create your views here.

def rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника шириной {width} и длинной {height} равна - {width * height}.")


def square_area(request, width: int):
    return HttpResponse(f"Площадь квадрата со стороной {width} равна - {width * width}.")


def circle_area(request, radius: int):
    return HttpResponse(f"Площадь круга радиусом {radius} равна - {pi * radius * radius}")


def get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square_area(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}/')


def get_circle_area(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}/')
