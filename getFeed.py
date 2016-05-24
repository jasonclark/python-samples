#!/usr/bin/env python

#get feed data from url
import requests
import sys
import xml.dom.minidom

#URI of the feed
URI = sys.argv[1] if len(sys.argv) > 1 else 'http://www.npr.org/rss/rss.php?id=1019'
#URI = 'http://www.npr.org/rss/rss.php?id=1019'
#if len(sys.argv) > 1:
    #URI = sys.argv[1]

#get feed data source
request = requests.get(URI)

#check for HTTP codes other than 200
if request.status_code != 200:
    print('Status:', request.status_code, 'Problem with the request. Exiting.')
    exit()

#actual xml document
document = xml.dom.minidom.parse(request.text)

#create empty string to store information
info = ""

#parse feed elements
for item in document.getElementsByTagName('item'):
    title = item.getElementsByTagName('title')[0].firstChild.data
    link = item.getElementsByTagName('link')[0].firstChild.data
    description = item.getElementsByTagName('description')[0].firstChild.data
    #format string as html and display
    info_str = '''<li><a title="%s" href="%s">%s</a></li>\n''' % \
        (title.encode('UTF8','replace'),
        link.encode('UTF8', 'replace'),
        description.encode('UTF8','replace'))
    #concatenate all html into one string for printing
    info += info_str

#show result as HTML
print '<ul>'
print(info)
print '</ul>'
