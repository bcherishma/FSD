from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def app_name(request):
    return HttpResponse("<h1> This is an Application </h1>")

def template_data(request):
    name="CMRIT"
    a=["abc","def","ghi"]
    return render(request,"template2.html",{"backend_data":name,"a":a})