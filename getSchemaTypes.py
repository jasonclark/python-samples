#!/usr/bin/env python

from bs4 import BeautifulSoup
import csv
import json
import os
import requests
#import urllib
import sys

#URI of the data source
URI = sys.argv[1] if len(sys.argv) > 1 else 'https://arc.lib.montana.edu/ivan-doig/about.php'
#URI = 'https://arc.lib.montana.edu/ivan-doig/about.php'
#if len(sys.argv) > 1:
    #URI = sys.argv[1]

def parse_source(uri):
    request = requests.get(uri, headers={'User-Agent' : 'jasonclark.info indexing bot'})
    #request = requests.get(uri, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
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
        aboutList.append({"about": tagValue, "length": len(tagValue)})

    #create json file if it doesn't exist, open and write parsed values into it
    if not os.path.exists(pageTitle+'-about.json'):
        open(pageFileName+'-about.json', 'w').close()
    
    with open(pageFileName+'-about.json', 'r+') as jsonFile:
        json.dump(skillList, jsonFile, indent = 4)

    jsonFile.close()

    #create csv file if it doesn't exist, open and write parsed values into it
    if not os.path.exists(pageTitle+'-about.csv'):
        open(pageFileName+'-about.csv', 'w').close()

    with open(pageFileName+'-about.csv', 'r+') as csvFile:
        writeFile = csv.writer(csvFile)
        writeFile.writerow(skillList)

    csvFile.close()

    #set empty list for type json values
    typeList = []

    #for dblink in soup.find_all('link', attrs={'property':'additionalType'}):
    for dblink in soup.find_all(property='additionalType'):
        #print('additionalType data: \n' + dblink.get('resource'))
        print('additionalType data: \n' + dblink.string)
	#print json.dumps(dblink.string, indent = 4)
        typeList.append({"type": dblink.string, "length":len(dblink.string)})

    #create json file if it doesn't exist, open and write parsed values into it
    if not os.path.exists(pageTitle+'-types.json'):
        open(pageFileName+'-types.json', 'w').close()
    
    with open(pageFileName+'-types.json', 'r+') as jsonFile:
        json.dump(typeList, jsonFile, indent = 4)

    jsonFile.close()

showResult = parse_source(URI)
print showResult
print 'JSON and CSV files created.'
