import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import wikipedia



names=["Nicolas Sarkozy", "George Adam"]
age_data=[]

urls=[]
for i in names:
    suggestion=wikipedia.search(i, results=1)
    if suggestion=="":
        urls.append("none")
    else:
        url_=wikipedia.page(suggestion).url
        urls.append(url_)
    
#might need to adjust to make sure name matches page search using something like suggest[0]

    

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
                age_data.append(datawewant)
