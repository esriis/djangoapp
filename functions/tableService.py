#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:31:59 2021

@author: erlendsriis
"""


from dataclasses import dataclass
from dataclass_csv import DataclassReader, dateformat
import csv
import datetime
from blobdatabase.models import Client, Project, SubProject, Blob
import pytz
import django.conf
from django.utils.timezone import make_aware
from django.http import HttpResponse


def uploadTable(f,decode=False):
    if decode:
        f = (line.decode('utf8') for line in f)
        
    itemList = csv2List(f)
    
    naive_datetime = datetime.datetime.now()
    naive_datetime.tzinfo  # None

    django.conf.settings.TIME_ZONE  # 'UTC'
    aware_datetime = make_aware(naive_datetime)
    aware_datetime.tzinfo  # <UTC>

    tz = pytz.timezone('UTC')

    for item in itemList:

        # Client
        clientRef = Client.objects.filter(name=item.client)
        if clientRef.exists():
            c = clientRef[0]
        else:
            c = Client(name=item.client)
            c.save()

        # Project
        projectRef = Project.objects.filter(name=item.project,
                                              client__name=item.client)
        if projectRef.exists():
            p = projectRef[0]
        else:
            p = Project(name=item.project,client=c)
            p.save()

        # Subproject
        subProjectRef = SubProject.objects.filter(project__name=item.project,
                                            project__client__name=item.client,
                                            dataType=item.dataType)
        if subProjectRef.exists():
            s = subProjectRef[0]
        else:
            s = SubProject(dataType=item.dataType,project=p)
            s.save()

        # Blob
        blobRef = Blob.objects.filter(guid=item.guid)
        if blobRef.exists():
            blobRef.delete()
        b = Blob(name = item.name,
                    fullPath = item.fullPath,
                    modifiedDate = tz.localize(item.modifiedDate),
                    # createdDate = tz.localize(item.createdDate),
                    modifiedBy = item.modifiedBy,
                    # createdBy = item.createdBy,
                    guid = item.guid,
                    extension = item.extension,
                    subProject = s)
        b.save()
    






def deleteTable(f,decode=False):
    if decode:
        f = (line.decode('utf8') for line in f)
    itemList = csv2List(f)
    for item in itemList:
        Blob.objects.get(fullPath = item.fullPath).delete()
        
        
        
        
def writeTable():
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tableOut.csv"'
    
    dateformat = "%d/%m/%Y %H:%M:%S"

    blobList = Blob.objects.all()        
    writer = csv.writer(response, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['client','project','dataType','name','fullPath',
                          'modifiedDate','modifiedBy',
                          'guid','extension'])
    
    for blob in blobList:
        writer.writerow([blob.subProject.project.client,
                              blob.subProject.project,
                              blob.subProject.dataType,
                              blob.name,
                              blob.fullPath,
                              blob.modifiedDate.strftime(dateformat),
                              # blob.createdDate.strftime(dateformat),
                              blob.modifiedBy,
                              # blob.createdBy,
                              blob.guid,
                              blob.extension])
            
    return response





def csv2List(f):
    @dataclass
    @dateformat('%d/%m/%Y %H:%M:%S')
    class fileItem:
        client: str
        project: str
        dataType: str
        name: str
        fullPath: str
        modifiedDate: datetime.datetime
        # createdDate: datetime.datetime
        modifiedBy: str
        # createdBy: str
        guid: str
        extension: str


    reader = DataclassReader(f,fileItem)    
    itemList = list(reader)
    return itemList




