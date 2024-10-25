from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app1/',views.app_name),
    path('data/', views.app_name, name = "Appplication 2"),
    path('templates/', views.template_data, name = "Template Data")
]