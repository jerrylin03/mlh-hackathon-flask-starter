# -*- coding: utf-8 -*-
import csv

saleToListVA = {}
with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\SaleToListRatio_City.csv') as csv_file:
    vaEstate = csv.DictReader(csv_file)
    for va in vaEstate:
        if (va['StateName'] == "VA"):
            saleToListVA[va['RegionName']] = va['2019-11']
print(saleToListVA)
saleToList_file = open("stoLVA.csv", "w")
ratioWriter = csv.writer(saleToList_file)

ratioWriter.writerow(["CityName", "Ratio"])
for key, value in saleToListVA.items():
    ratioWriter.writerow([key, value])

saleToList_file.close()