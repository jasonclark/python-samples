#!/usr/bin/env python

import json
import requests
import sys

#URI of the JSON data source
URI = sys.argv[1] if len(sys.argv) > 1 else 'https://kgsearch.googleapis.com/v1/entities:search?query=library&limit=25&indent=1&key=ADD-KNOWLEDGE-GRAPH-API-KEY'

#get json data
request = requests.get(URI)

#check for HTTP codes other than 200
if request.status_code != 200:
    print('Status:', request.status_code, 'Problem with the request. Exiting.')
    exit()

#convert into a python object
#data = request.json()
data = json.loads(request.text)

#pretty print JSON for diagnostics 
#print json.dumps(data, indent=4, sort_keys=True)

#for each element, item, in data.itemListElement,
for item in data['itemListElement']:
    #print name, id, and short description
    print (item['result']['name'], item['result']['@id'], item['result']['description'])
