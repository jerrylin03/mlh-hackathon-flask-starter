# -*- coding: utf-8 -*-

import csv

with open('C:\\Users\\espos\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\AllRegionsForePublic.csv') as csv_file:
    countyEstate = csv.DictReader(csv_file)
    countyDict = {}
    for county in countyEstate:
        if (county['StateName'] == 'VA'):
            if (county['CountyName'] != ''):
                countyDict[county['CountyName']] = county['ForecastYoYPctChange']
    print(countyDict)
    
county_file = open("countyVA.csv", "w")
countyWriter = csv.writer(county_file)
countyWriter.writerow(['County', 'Forecast Percentage'])
for key, value in countyDict.items():
    countyWriter.writerow([key, value])
county_file.close()