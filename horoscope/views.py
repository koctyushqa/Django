from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

elements_dict = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "scorpio", "pisces"],
}


def index(request):
    zodiacs = list(zodiac_dict)

    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f"<li> <a href={redirect_path}> {sign.title()} </a> </li>"
    response = f'''
    <ol>
        {li_elements}
    </ol>
    '''
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:  # Если ввели что-то, что равно одному из ключей(key) в словаре, то возвращаем значение(value) этого ключа.
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Неизвестный знак задиака - {sign_zodiac}.")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(
            f"Вы выбрали несуществующий знак - {sign_zodiac}. Существует только 12 знаков Зодиака.")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_info_about_type(request):
    elements = list(elements_dict)
    li_elements = ''
    for sign in elements:
        redirect_path_elements = reverse("elements-name", args=[sign])
        li_elements += f"<li> <a href={redirect_path_elements}> {sign.title()} </a> </li>"
    response = f'<ul> {li_elements} </ul>'
    return HttpResponse(response)


def get_info_about_elements(request, sign_type: str):
    result = "Такой стихии не существует."
    if sign_type in elements_dict:
        result = ''
        for i in elements_dict[sign_type]:
            redirect_path_zodiacs = reverse("horoscope-name", args=[i])
            result += f"<li> <a href={redirect_path_zodiacs}> {i.title()} </a> </li>"
    return HttpResponse(f'<ul> {result} </ul>')


def determine_sign_by_date(request, month: int, day: int):
    result = HttpResponseNotFound("Некорректная дата.")
    if month > 12 or day > 31:
        return result
    else:
        if (month == 3 and day >= 21) or (month == 4 and day <= 20):
            result = 'aries'
        elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
            result = 'taurus'
        elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
            result = 'gemini'
        elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
            result = 'cancer'
        elif (month == 7 and day >= 23) or (month == 8 and day <= 23):
            result = 'leo'
        elif (month == 8 and day >= 24) or (month == 9 and day <= 23):
            result = 'virgo'
        elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
            result = 'libra'
        elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
            result = 'scorpio'
        elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
            result = 'sagittarius'
        elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
            result = 'capricorn'
        elif (month == 1 and day >= 21) or (month == 2 and day <= 18):
            result = 'aquarius'
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            result = 'pisces'

        url_sign = reverse('horoscope-name', args=[result])
        return HttpResponse(f'Месяц: {month}. День: {day}. Соответствует знаку Зодиака - <a href={url_sign}>{result}</a>.')
