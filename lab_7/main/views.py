from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h4>Оппа1</h4>")

def about(request):
    return HttpResponse("<h4>Оппа2</h4>")