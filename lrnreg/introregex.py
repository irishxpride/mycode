#!/usr/bin/python3
import urllib.request
import re

print ("Where should we search? ")
url = input()
print ("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()

searchMe = urllib.request.urlopen(url).read().decode("utf-8")
searchResults = []

if re.findall(searchFor, searchMe):
    print(f"Found " + re.findall(searchFor, searchMe)  + " match!")
else:
    print("No Match...")
