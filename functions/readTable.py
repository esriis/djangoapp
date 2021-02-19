#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:31:59 2021

@author: erlendsriis
"""


from dataclasses import dataclass
from dataclass_csv import DataclassReader, dateformat
import datetime
from newApp.models import Client, Building, Project, Blob
import pytz
import django.conf
from django.utils.timezone import make_aware


def readTable():
    naive_datetime = datetime.datetime.now()
    naive_datetime.tzinfo  # None

    django.conf.settings.TIME_ZONE  # 'UTC'
    aware_datetime = make_aware(naive_datetime)
    aware_datetime.tzinfo  # <UTC>

    tz = pytz.timezone('Europe/Oslo')

    filename = "/Users/erlendsriis/Documents/sannsyn/consigli/python/sh"+\
        "arepointTest/powershell-script/test.csv"


    @dataclass
    @dateformat('%d/%m/%Y %H:%M:%S')
    class fileItem:
        client: str
        building: str
        project: str
        name: str
        fullPath: str
        modifiedDate: datetime.datetime
        createdDate: datetime.datetime
        modifiedBy: str
        createdBy: str
        guid: str
        extension: str



    with open(filename) as users_csv:
        reader = DataclassReader(users_csv, fileItem)
        itemList = list(reader)

    for item in itemList:

        # Client
        clientRef = Client.objects.filter(name=item.client)
        if clientRef.exists():
            c = clientRef[0]
        else:
            c = Client(name=item.client)
            c.save()

        # Building
        buildingRef = Building.objects.filter(name=item.building,
                                              client__name=item.client)
        if buildingRef.exists():
            b = buildingRef[0]
        else:
            b = Building(name=item.building,client=c)
            b.save()

        # Project
        projectRef = Project.objects.filter(building__name=item.building,
                                            building__client__name=item.client,
                                            name=item.project)
        if projectRef.exists():
            p = projectRef[0]
        else:
            p = Project(name=item.project,building=b)
            p.save()

        # Blob
        blobRef = Blob.objects.filter(fullPath=item.fullPath)
        if blobRef.exists():
            blobRef.delete()
        blob = Blob(name = item.name,
                    fullPath = item.fullPath,
                    modifiedDate = tz.localize(item.modifiedDate),
                    createdDate = tz.localize(item.createdDate),
                    modifiedBy = item.modifiedBy,
                    createdBy = item.createdBy,
                    guid = item.guid,
                    extension = item.extension,
                    project = p)
        blob.save()

