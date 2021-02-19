from django.shortcuts import render
from django.http import HttpResponse
from functions.readTable import readTable
from pathlib import Path


def index(request):
    return HttpResponse("Hello, world. You're at the blobstore index.")

def update_view(request):
    tablePath = Path("../input/tableIn.csv")
    if tablePath.is_file():
        readTable()
        return HttpResponse("Updated")
    else:
        return HttpResponse("No file found")
