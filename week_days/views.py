from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_dict = {
    "monday": "Monday (понедельник) — назван в честь богини Луны (Moon).",
    "tuesday": "Tuesday (вторник) — назван в честь однорукого бога воинской доблести Тюра.",
    "wednesday": "Wednesday (среда) — «день Одина», назван в честь верховного бога Одина.",
    "thursday": "Thursday (четверг) — назван в честь сына Одина, Тора, того самого Тора с молотом.",
    "friday": "Friday (пятница) — назван в честь жены Одина, Фригги, богини замужней любви.",
    "saturday": "Saturday (суббота) — назван в честь древнеримского бога Сатурна.",
    "sunday": "Sunday (воскресенье) — назван в честь бога Солнца (Sun).",
}


def info_about_week_days(request, day: str):
    description = days_dict.get(day, None)
    if day:  # Если ввели что-то, что равно одному из ключей(key) в словаре, то возвращаем значение(value) этого ключа.
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"{day} - такого дня недели не существует.")


def info_about_week_days_by_number(request, day: int):
    day_list = list(days_dict)
    if day > len(day_list):
        return HttpResponseNotFound(f"Неверный номер дня - {day}. Существует только 7 дней недели.")
    name_day = day_list[day - 1]
    redirect_url = reverse("days-name", args=[name_day])
    return HttpResponseRedirect(redirect_url)
