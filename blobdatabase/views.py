from django.shortcuts import render
from django.http import HttpResponse
from functions.readTable import readTable
from pathlib import Path


def index(request):
    return HttpResponse("Hello, world. You're at the blobstore index.")

def update_view(request):
    tablePath = Path("tables/tableIn.csv")
    newString = tablePath.absolute().as_posix()
    if tablePath.is_file():
        response = readTable()
        return HttpResponse(response)
    else:
        return HttpResponse("No file uploaded.")
