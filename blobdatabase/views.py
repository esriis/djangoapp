from django.shortcuts import render
from django.http import HttpResponse
from functions.readTable import readTable


def index(request):
    return HttpResponse("Hello, world. You're at the blobstore index.")

def update_view(request):
    readTable()
    return HttpResponse("Welcome to my world")
