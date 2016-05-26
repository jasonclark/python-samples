#!/usr/bin/env python

from xml.etree.ElementTree import parse
import requests
import sys

#URI of the feed
URI = sys.argv[1] if len(sys.argv) > 1 else 'http://www.npr.org/rss/rss.php?id=1019'

#get feed data source
request = requests.get(URI, stream=True)

#check for HTTP codes other than 200
if request.status_code != 200:
    print('Status:', request.status_code, 'Problem with the request. Exiting.')
    exit()

#parse data feed
data = parse(request.raw)

#create empty string to store HTML
document = ''

#extract and output tags
for item in data.iterfind('channel/item'):
    title = item.findtext('title')
    description = item.findtext('description')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    markup = '<li><a href="'+link+'">'+title+ '-' +description+ '('+date+')</a></li>\n'
    document += markup

#show result as HTML
print '<ul>\n'
print(document)
print '<ul>\n'
