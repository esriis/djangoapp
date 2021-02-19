from django.shortcuts import render
from django.http import HttpResponse
from functions.readTable import readTable
from functions.writeTable import writeTable
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
    
def write_view(request):
    tablePath = Path("tables/tableOut.csv")
    if tablePath.is_file():
        return HttpResponse("Table already exists.")
    else:
        writeTable()
        return HttpResponse("Did this work?")
        
    
   
