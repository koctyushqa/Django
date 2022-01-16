from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.info_about_week_days_by_number),
    path('<str:day>/', views.info_about_week_days),
]
