from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return HttpResponse (request,"hello/index.html")
# def akshit(request):
#     return HttpResponse ("Hi Akshit")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })