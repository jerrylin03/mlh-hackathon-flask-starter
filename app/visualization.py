# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:00:36 2020

@author: 2k
"""
import csv

#parsing csv file of city names, longitude, latitude, and sale-to-list price ratio
with open('C:\\Users\\2k\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\cityVA.csv', 'r') as csvFile:
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

#print(name)
#print(lat)
#print(long)
#print(ratio)

#importing of plotting libraries
import os
os.environ["PROJ_LIB"] = r'C:\Users\2k\Anaconda3\Library\share'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import cm
#conversion of string to float
x = []
y = []
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


#label every plot point with a city name
#for i, txt in enumerate(name):
 #   plt.annotate(txt, (x[i], y[i]))

#zoom in to the state of virginia
fig = plt.figure(figsize=(48,8))
map = Basemap(projection='cyl', llcrnrlon = -84.5, llcrnrlat = 36.23, urcrnrlon = -75.15, urcrnrlat = 39.77, resolution = 'h', epsg = 2924)
map.drawstates(linewidth = 0.25)
map.drawcoastlines(linewidth = 0.25)

map.readshapefile('C:\\Users\\2k\\Documents\\GitHub\\mlh-hackathon-flask-starter\\app\\datasets\\us-zip-code-latitude-and-longitude\\us-zip-code-latitude-and-longitude', 'us-zip-code-latitude-and-longitude')

#plot coordinates onto a scatter plot    
x, y = map(long, lat)

plt.scatter(x, y, c=norm, cmap= 'viridis')
plt.title("Virginia Property Sale-to-List Price Ratios per City (Purple = Low --> Blue = Medium/Average --> Green = High --> Yellow = Highest)")

#pos = plt.imshow(1, vmin = ratioMin, vmax = ratioMax)
#fig.colorbar(pos)

plt.show()


#ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
#ax.add_collection3d(map.drawcountries(linewidth=0.35))
