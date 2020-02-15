# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:00:36 2020

@author: 2k
"""
import geopandas as gpd
#from shapely.geometry import Point, polygon
#import matplotlib.pyplot as plt
#import pandas as pd
#geocode from geopandas library
from geopandas.tools import geocode


usa = gpd.read_file('C:\Users\2k\Anaconda3\pkgs\geopandas-0.6.3-py_0\site-packages\geopandas\datasets\naturalearth_cities.shp')
usa.plot()
#usa[usa.STATE_ABBR == 'VA'].plot()


#plot all cities on map with longitude and lattitude coordinates
cities = ['Blacksburg, VA', 'Burke, VA', 'Springfield, VA', 'Reston, VA', 'Sterling, VA']

for i in range (0, len(cities)):
    coor = geocode(cities[i])
    print(coor)
