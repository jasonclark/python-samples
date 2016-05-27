#!/usr/bin/env python

from bs4 import BeautifulSoup
import json
import requests
#import urllib
import sys

#URI of the data source
URI = sys.argv[1] if len(sys.argv) > 1 else 'https://arc.lib.montana.edu/ivan-doig/about.php'
#URI = 'https://arc.lib.montana.edu/ivan-doig/about.php'
#if len(sys.argv) > 1:
    #URI = sys.argv[1]

def parseSource(uri):
    request = requests.get(uri, headers={'User-Agent' : 'jasonclark.info indexing bot'})
    #request = urllib.urlopen(uri).read()

    #check for HTTP codes other than 200
    if request.status_code != 200:
        print('Status:', request.status_code, 'Problem with the request. Exiting.')
        exit()

    soup = BeautifulSoup(request.text, 'html.parser')
    #soup = BeautifulSoup(request, 'html.parser')
    #print soup.findAll('a')
    #print soup.prettify()
    #print(soup.get_text())

    title = soup.title.string

    print ('Page Title: \n' + title)
    print ('Page URL: \n' + uri)

    #for link in soup.find_all('a', attrs={'property':'about'}):
    for link in soup.find_all(property='about'):
        #print('about data: \n' + link.get('href'))
        print('about data: \n' + link.string)

    #for dblink in soup.find_all('link', attrs={'property':'additionalType'}):
    for dblink in soup.find_all(property='additionalType'):
        #print('additionalType data: \n' + dblink.get('resource'))
        print('additionalType data: \n' + dblink.string)
    
def makeSource(uri):
    request = requests.get(uri, headers={'User-Agent' : 'jasonclark.info indexing bot'})

    #check for HTTP codes other than 200
    if request.status_code != 200:
        print('Status:', request.status_code, 'Problem with the request. Exiting.')
        exit()

    #convert json into python object
    jsonFile = json.loads(request.text)

    with open('json-kg-sample.txt', 'w') as outfile:
        json.dump(jsonFile, outfile, sort_keys = True, indent = 4)

showResult = parseSource(URI)
print showResult

createFile = makeSource(URI)
print 'JSON file created.'
