# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#adds to saleToListVA dictionary
cityList = []
ratioList = []
ratioCity = {}
with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\SaleToListRatio_City.csv') as csv_file:
    vaEstate = csv.DictReader(csv_file)
    for va in vaEstate:
        if (va['StateName'] == "VA"):
            ratioList.append(va['2019-11'])
            cityList.append(va['RegionName'])
            ratioCity[va['RegionName']] = va['2019-11']
x = 0
latVA = []
longVA = []
city_file = open("cityVA.csv", "w")
cityWriter = csv.writer(city_file)
cityWriter.writerow(['CityName', 'Latitude', 'Longitude', 'S/L Ratio'])
with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\us-zip-code-latitude-and-longitude\\va-zip-code-latitude-and-longitude.csv') as csv_file2:
    csvValues = []
    vaCity = csv.DictReader(csv_file2)
    for urban in vaCity:
        csvValues = urban['Zip;City;State;Latitude;Longitude;Timezone;Daylight savings time flag;geopoint'].split(';')
        for i in cityList:
            if (i == csvValues[1]):
                #print(i)
                print(csvValues[1] + " " + csvValues[3] + " " + csvValues[4])
#                print(float(csvValues[3]))
#                print(float(csvValues[4]))
                latVA.append(float(csvValues[3]))
                longVA.append(float(csvValues[4]))
                cityWriter.writerow([csvValues[1], csvValues[3], csvValues[4], ratioCity[csvValues[1]]])
city_file.close()
