# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:00:36 2020

@author: Tukhang Trinh
"""
import os
import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import geopandas as gpd

#importing of plotting libraries specific to Anaconda
os.environ["PROJ_LIB"] = r'.\Anaconda3\Library\share'

#parsing csv file of city names, longitude, latitude, and sale-to-list price ratio
with open('datasets\\cityVA.csv', 'r') as csvFile:
#with open('.\cityVA.csv', 'r') as csvFile:
    name = []
    lat = []
    long = []
    ratio = []
    
    reader = csv.DictReader(csvFile)
    
    for line in reader:
        if line['CityName'] != '':
            name.append(line['CityName'])
            lat.append(line['Latitude'])
            long.append(line['Longitude'])
            ratio.append(line['S/L Ratio'])

#end with


#conversion of string to float
num = len(long)

for i in range(0, num):
    long[i] = float(long[i])
    lat[i] = float(lat[i])
    ratio[i] = float(ratio[i])
   
#normal distribution, min, and max calculations
norm = []
    
ratioMin = min(ratio)
ratioMax = max(ratio)

for i in range(0, num):
    normNum = float((ratio[i]-ratioMin)/(ratioMax-ratioMin))
    norm.append(normNum)

#basemap library's version of plotting Virginia(other state borders included)
#fig = plt.figure(figsize=(48,8))
#map = Basemap(projection='cyl', llcrnrlon = -84.5, llcrnrlat = 36.23, urcrnrlon = -75.15, urcrnrlat = 39.77, resolution = 'h', epsg = 2924)
#map.drawstates(linewidth = 0.25)
#map.drawcoastlines(linewidth = 0.25)

#geopandas version of plotting the map of Virginia
usa = gpd.read_file('./states_21basic/states.shp')
va = usa[usa.STATE_ABBR == 'VA'].plot(figsize = (48,8), facecolor = 'white', edgecolor = 'black', linewidth = 0.25)

#read shape file of all zip codes in Virginia
#map.readshapefile('C:\\Users\\2k\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\us-zip-code-latitude-and-longitude\\us-zip-code-latitude-and-longitude', 'us-zip-code-latitude-and-longitude')

#plot coordinates onto a scatter plot 
#x = []
#y = []   
#x, y = map(long, lat)

plt.scatter(long, lat, c=norm, cmap= 'viridis', s = 20)
plt.title("Virginia Home Property Sale-to-List Price Ratios per City \n", fontsize = 15)
plt.xlabel('Longitude (degrees W) \n\n\n| Yellow = Highest |\n| Green = High |\n| Blue = Medium |\n| Purple = Low |\n| Black = Lowest |', fontsize=12)
plt.ylabel('Latitude (degrees N)', fontsize=12)

#label every plot point with a city name
#for i, txt in enumerate(name):
    #plt.annotate(txt, (x[i], y[i]))

#color bar legend
#pos = plt.imshow(1, vmin = ratioMin, vmax = ratioMax)
#fig.colorbar(pos)

plt.show()
