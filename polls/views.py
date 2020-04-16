# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home</h1>")
def test(request):
    return HttpResponse("<h1>Test</h1>")
def page(request):
    return HttpResponse("<h1>Page</h1>")