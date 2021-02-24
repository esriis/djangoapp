"""azuresite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blobdatabase.views import download_view, upload_view, delete_view, deleteFTP_view, uploadFTP_view

urlpatterns = [
    path('upload',upload_view),
    path('delete',delete_view),
    path('deleteFTP',deleteFTP_view),
    path('deleteFTP',uploadFTP_view),
    path('download',download_view),
    path('blobdatabase/', include('blobdatabase.urls')),
    path('admin/', admin.site.urls),
]
