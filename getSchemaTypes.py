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

    #set empty list for about json values
    aboutList = [] 

    #for link in soup.find_all('a', attrs={'property':'about'}):
    for link in soup.find_all(property='about'):
        #print('about data: \n' + link.get('href'))
        tagValue = link.string.strip('\r\n\t')
        print('about data: \n' + tagValue)
        aboutList.append((tagValue, len(tagValue)))
	
    with open('json-schema-about.txt', 'w') as outfile:
            json.dump(aboutList, outfile, indent = 4)

    #set empty list for type json values
    typeList = []

    #for dblink in soup.find_all('link', attrs={'property':'additionalType'}):
    for dblink in soup.find_all(property='additionalType'):
        #print('additionalType data: \n' + dblink.get('resource'))
        print('additionalType data: \n' + dblink.string)
	#print json.dumps(dblink.string, indent = 4)
        typeList.append((dblink.string, len(dblink.string)))

    with open('json-schema-types.txt', 'w') as outfile:
        json.dump(typeList, outfile, indent = 4)

showResult = parseSource(URI)
print showResult
print 'JSON files created.'
