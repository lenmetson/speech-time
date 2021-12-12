"""
Created on Sun Dec 12 16:06:06 2021

@author: noemieclaret
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:23:58 2021

@author: noemieclaret
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import wikipedia
import re
import csv

feliz_navidad=[]
with open('/Users/noemieclaret/Desktop/feliz_navidad.csv') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',')
    for row in my_reader:
        feliz_navidad.append(row)

names=[]
for row in feliz_navidad:
    name=row[5]
    names.append(name)
    


age_data=[]

urls=[]
for i in names:
    search_sug=wikipedia.search(i, results=1, suggestion=False)
    url_=wikipedia.page(search_sug[0], auto_suggest=False).url
    urls.append(url_)
    
    

for url in urls:
    if url=="none":
        age_data.append("none")
    else:    
        html = urlopen(url) 
        soup = BeautifulSoup(html, 'html.parser')
        left=soup.find_all("th", class_="infobox-label")
        for left_element in left:
            if left_element.text=="Born":
                datawewant=left_element.find_next_sibling("td").text
                age_data.append(str(datawewant))
