from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app1/',views.app_name),
    path('data/', views.app_name, name = "Appplication 1"),
    path('template6/', views.template_data, name = "Template Data"),
    path('apidata/',views.api_data,name="Api Data"),
    path('comments/',views.comments,name="Comments Data"),
    path('Handle/',views.handle_form,name="Handle Form")
]