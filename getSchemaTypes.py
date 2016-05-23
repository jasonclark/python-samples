#!/usr/bin/env python

from bs4 import BeautifulSoup
#import json
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

    soup = BeautifulSoup(request.text, 'html.parser')
    #soup = BeautifulSoup(request, 'html.parser')
    #print soup.findAll('a')
    #print soup.prettify()
    #print(soup.get_text())

    title = soup.title.string

    print ('Page URL: \n' + uri)

    print ('Page Title: \n' + title)

    #for link in soup.find_all('a', attrs={'property':'about'}):
    for link in soup.find_all(property='about'):
        print('about link: \n' + link.get('href'))

    #for dblink in soup.find_all('link', attrs={'property':'additionalType'}):
    for dblink in soup.find_all(property='additionalType'):
        print('additionalType link: \n' + dblink.get('resource'))
    
showResult = parseSource(URI)
print showResult
