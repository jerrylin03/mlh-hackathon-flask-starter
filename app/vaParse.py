# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#adds to saleToListVA dictionary
cityList = []
ratioList = []
with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\SaleToListRatio_City.csv') as csv_file:
    vaEstate = csv.DictReader(csv_file)
    for va in vaEstate:
        if (va['StateName'] == "VA"):
            ratioList.append(va['2019-11'])
            cityList.append(va['RegionName'])
#print(ratioList)
#print(cityList)
#saleToList_file = open("stoLVA.csv", "w")
#ratioWriter = csv.writer(saleToList_file)
#
#ratioWriter.writerow(["CityName", "Ratio"])
#for key, value in saleToListVA.items():
#    ratioWriter.writerow([key, value])
#
#saleToList_file.close()

latVA = []
longVA = []
with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\docs\\us-zip-code-latitude-and-longitude\\va-zip-code-latitude-and-longitude.csv') as csv_file2:
    csvValues = []
    vaCity = csv.DictReader(csv_file2)
    for urban in vaCity:
        csvValues = urban['Zip;City;State;Latitude;Longitude;Timezone;Daylight savings time flag;geopoint'].split(';')
        for i in cityList:
            if (i == csvValues[1]):
                print(i)
                print(csvValues[1])
                print(float(csvValues[3]))
                print(float(csvValues[4]))
                latVA.append(float(csvValues[3]))
                longVA.append(float(csvValues[4]))

city_file = open("cityVA.csv", "w")
cityWriter = csv.writer(city_file)
cityWriter.writerow(['CityName', 'Latitude', 'Longitude', 'S/L Ratio'])
x = 0
for i in cityList:
    cityWriter.writerow([i, latVA[x], longVA[x], ratioList[x]])
    x = x + 1
    
#print(longVA)
  
#print(saleToListVA.items())
#print(cityList)
#for i in saleToListVA.keys():
#    print(saleToListVA[i])
    
#location_file = open("locateVA.csv")
#locateWriter.writerow(['CityName', 'Latitude', 'Longitude', 'Sales-To-List Ratio'])
#for k, v in locateVa.items():
#    
#    locateWriter.writeRow([k, v[0], v[1, ]])

