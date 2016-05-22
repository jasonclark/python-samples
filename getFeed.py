#!/usr/bin/env python

# get feed data from url
import urllib
import sys
import xml.dom.minidom

# URI of the feed
URI = 'https://www.npr.org/rss/rss.php?id=1019'

# actual xml document
document = xml.dom.minidom.parse(urllib.urlopen(URI))

# create empty string to store information
info = ""

# parse feed elements
for item in document.getElementsByTagName('item'):
    title = item.getElementsByTagName('title')[0].firstChild.data
    link = item.getElementsByTagName('link')[0].firstChild.data
    description = item.getElementsByTagName('description')[0].firstChild.data
    # format string as html and display
    info_str = '''<li><a title="%s" href="%s">%s</a></li>\n''' % \
        (title.encode('UTF8','replace'),
        link.encode('UTF8', 'replace'),
        description.encode('UTF8','replace'))
    # concatenate all html into one string for printing
    info += info_str

# check result
print "<ul>"
print(info)
print "</ul>"
