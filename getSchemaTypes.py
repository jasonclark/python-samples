#!/usr/bin/env python

from bs4 import BeautifulSoup
#import json
import requests
#import urllib
import re
import sys

#hardcode URI to request
#URI = 'https://arc.lib.montana.edu/ivan-doig/about.php'
#allow URI to be passed to script
URI = sys.argv[1]

def parseSource(uri):
    request = requests.get(uri, headers={'User-Agent' : 'jasonclark.info indexing bot'})
    #request = urllib.urlopen(uri).read()

    soup = BeautifulSoup(request.text, 'html.parser')
    #soup = BeautifulSoup(request, 'html.parser')
    #print soup.findAll('a')
    #print soup.prettify()
    #print(soup.get_text())

    title = soup.title.string

    print ('Page URL: \n' + uri)

    print ('Page Title: \n' + title)

    #for link in soup.find_all(property=re.compile("additionalType")):
    for link in soup.find_all('a', attrs={'property':'about'}):
        print('Wikipedia link: \n' + link.get('href'))

    #for dblink in soup.find_all(property=re.compile("additionalType")):
    for dblink in soup.find_all('link', attrs={'property':'additionalType'}):
        print('Dbpedia link: \n' + dblink.get('resource'))
    
showResult = parseSource(URI)
print showResult
