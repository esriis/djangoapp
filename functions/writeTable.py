#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:56:18 2021

@author: erlendsriis
"""


import csv
from blobdatabase.models import Blob
from django.http import HttpResponse


def writeTable():
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tableOut.csv"'
    
    dateformat = "%d/%m/%Y %H:%M:%S"

    blobList = Blob.objects.all()        
    writer = csv.writer(response, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['client','building','project','name','fullPath',
                          'modifiedDate','createdDate','modifiedBy',
                          'createdBy','guid','extension'])
    
    for blob in blobList:
        writer.writerow([blob.project.building.client,
                              blob.project.building,
                              blob.project.name,
                              blob.name,
                              blob.fullPath,
                              blob.modifiedDate.strftime(dateformat),
                              blob.createdDate.strftime(dateformat),
                              blob.modifiedBy,
                              blob.createdBy,
                              blob.guid,
                              blob.extension])
            
    return response
