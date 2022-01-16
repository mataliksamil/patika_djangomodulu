from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> INDEX SAYFASI </h1>")