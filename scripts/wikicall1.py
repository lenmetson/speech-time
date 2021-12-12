#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
                
                
                
#now take year from age data
born_year=[]
for i in age_data:
    if i=="none":
        born_year.append("none")
    else:
        year=re.match(r'.*([1-3][0-9]{3})', i).group(1)
        born_year.append(year)
        
        
      
