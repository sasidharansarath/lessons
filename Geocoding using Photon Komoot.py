#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd

address = raw_input("Enter the first few lines of address/location: ")

address_new = address.replace(" ","+")

url_loc = "http://photon.komoot.de/api/?q="+address_new+"&limit=1"

location = requests.get(url_loc, params = None)

print
print location.url

location_data = location.json()

loc_lon = location_data['features'][0]['geometry']['coordinates'][0]
loc_lat = location_data['features'][0]['geometry']['coordinates'][1]

# print address_new
# print location_data
print
print 'Location: ',address
print 'Longitude: ',loc_lon
print 'Latitude: ',loc_lat


# In[ ]:





# In[ ]:




