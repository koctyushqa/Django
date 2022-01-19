from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_info_about_type),
    path('<int:month>/<int:day>/', views.determine_sign_by_date),
    path('type/<str:sign_type>/', views.get_info_about_elements, name="elements-name"),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name="horoscope-name"),
]
