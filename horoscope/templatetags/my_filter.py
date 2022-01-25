# from django import template
# from django.template.defaultfilters import stringfilter
#
# register = template.Library()
#
#
# @register.filter(name='split')
# @stringfilter     # Если нужно гарантировать что в value будет строка(импорт нужен). В остальных случаях будет ошибка.
# def split(value, key=' '):
#     return value.split(key)

# В info_zodiac.html написать {% load my_filter %} (Важно! Нужно указывать название именно .py ФАЙЛА)
# В <h1> заменить - Приложение Гороскоп - на {{ description_zodiac|split|first }}
