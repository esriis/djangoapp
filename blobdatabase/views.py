from django.shortcuts import render
from django.http import HttpResponse
from functions.tableService import updateTable, deleteTable, writeTable
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# from .forms import UploadFileForm


def index(request):
    return HttpResponse("Hello, world. You're at the blobdatabase index.")


@csrf_exempt
def download_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = writeTable()
            logout(request)
            return(response)
        else:
            return HttpResponse("Login unsuccessful.")
    else:
        return HttpResponse("Login details required.")
    
    
@csrf_exempt
def upload_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # form = UploadFileForm(request.POST, request.FILES)
            # print(form.title)
            # print(form.file)
            # if form.is_valid():
            response = updateTable(request.FILES['file'])
            # else:
            #     response = "Uh oh."
            logout(request)
            return HttpResponse(response)
        else:
            return HttpResponse("Login unsuccessful.")
    else:
        return HttpResponse("Requires POST")
    
    
    
@csrf_exempt
def delete_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # form = UploadFileForm(request.POST, request.FILES)
            # print(form.title)
            # print(form.file)
            # if form.is_valid():
            response = deleteTable(request.FILES['file'])
            # else:
            #     response = "Uh oh."
            logout(request)
            return HttpResponse(response)
        else:
            return HttpResponse("Login unsuccessful.")
    else:
        return HttpResponse("Requires POST")
