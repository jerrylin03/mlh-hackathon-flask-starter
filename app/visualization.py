# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:00:36 2020

@author: 2k
"""
import csv

#from mpl_toolkits.mplot3d import Axes3D

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

        
print(name)
print(lat)
print(long)
print(ratio)


    
#longitude and lagitude of zipcodes


import os
os.environ["PROJ_LIB"] = r'C:\Users\2k\Anaconda3\Library\share'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

x = []
y = []

for i in range(0, len(long)):
    long[i] = float(long[i])
    
for i in range(0, len(lat)):
    lat[i] = float(lat[i])
    
    
x, y = map(long, lat)
plt.plot(x, y, 'ro')


map = Basemap(projection='cyl', llcrnrlon = -84.7, llcrnrlat = 36.23, urcrnrlon = -75.15, urcrnrlat = 39.83, resolution = 'h', epsg = 2283)
map.drawstates(linewidth = 0.25)
map.drawcoastlines(linewidth = 0.25)


plt.show()

#map.drawstates(linewidth = 0.25)
#fig = plt.figure()
#ax = Axes3D(fig)

'''
ax.azim = 270
ax.elev = 90
ax.dist = 5
'''

#ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
#ax.add_collection3d(map.drawcountries(linewidth=0.35))
