from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('<h1>Hello World!</h1>')

def hello(request):
    print(request)
    return HttpResponse('<h1>Hello mens and girls!</h1>')

def test(request):
    return HttpResponse('<h3>Тестовая страница</h3>')