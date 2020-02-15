'''
Call the Zillow getSearchResults API and parse the information

@author: Jerry Lin, Tyler Esposo, TK
@date: 2/15/2020
'''
import requests
import json
import csv
import pandas

# insert your ZWSID
ZWSID = "X1-ZWz17dwf7615or_17jma"

url = 'http://www.zillow.com/webservice/GetSearchResults.htm?zws-id={}&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA'.format(ZWSID)

# make request to API
response = requests.get(url)

print(response.status_code)
