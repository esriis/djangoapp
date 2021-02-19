#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:56:18 2021

@author: erlendsriis
"""


import csv
from blobdatabase.models import Blob


def writeTable():
    
    filename = "tables/tableOut.csv"
    
    dateformat = "%d/%m/%y %H:%M:%S"

    blobList = Blob.objects.all()        
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['client','building','project','name','fullPath',
                              'modifiedDate','createdDate','modifiedBy',
                              'createdBy','guid','extension'])
        
        for blob in blobList:
            spamwriter.writerow([blob.project.building.client,
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
            

