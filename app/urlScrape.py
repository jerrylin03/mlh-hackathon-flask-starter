# -*- coding: utf-8 -*-

import csv

with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\properties-24060.csv') as csv_file:
    stringList = []
    zPid = []
    allPid = []
    blacksburgEstate = csv.DictReader(csv_file)
    for blacksburg in blacksburgEstate:
        stringList = blacksburg['url'].split('/')
        print(stringList[5])
        zPid.append(stringList[5])

    for i in range(len(zPid)):
        allPid.append(zPid[i].split('_')[0])
    
    print(allPid)