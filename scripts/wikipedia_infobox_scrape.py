
#here we parsed through the wikipedia infoboxes. But since this a is highly irregular storage method, we did not end up using this method.



import pandas as pd
import urllib.request
import numpy as np
import requests
from bs4 import BeautifulSoup
import wikipedia
import re
from urllib.request import urlopen



## Upload data from disk and convert csv to pandas DataFrame

print('-----------------------------------------------------------------')
print("Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.")
print('-----------------------------------------------------------------')

# LM: I will have a look at a way to set relative file paths in python
harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

## Subset table where the speeches are actually speeches

speech_table=harvard[:][harvard["is_speech"]==1]


## Get rid of the rows where the speaker does not have a parl_id or type

speech_table=speech_table[:][speech_table["parl_id"]!="NaN"].dropna(axis=0, how='any', subset=["wikidataid", "type"])
# LM: can we do this by dropping just those without parl_id, that feels more legit given it's our justification?

def find_unique_values(dataset, column, feature1, feature2, comment=True, dictionary=True):
    if feature1!="none":
        dataset=dataset[dataset[feature1]==feature2]
    unique_values=dataset[column].unique() #number of unique values
    if dictionary==True:
        val_dict= {idx:column for idx, column in enumerate(dataset[column].unique())}
        print(val_dict)
    if comment==True:
        print("The {} with the following filter: {} is {} are given below".format(column, feature1, feature2))
    return unique_values #return both number of unique values and the dictrionary containing them

#get unique wikiIDs

wiki=find_unique_values(speech_table, "wikidataid", feature1="none", feature2="none", comment=False, dictionary=False)

#get wikipage title from wikiID: firdst make API search request with url, parse through returned html
  
    
page_title={}

for wikiId in wiki:
    url="https://www.wikidata.org/w/api.php?action=wbgetentities&format=xml&props=sitelinks&ids={}&sitefilter=enwiki".format(wikiId)
    r=requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.sitelink["title"]
    page_title[wikiId]=result


#get correct url this way
age_data=[]

urls=[]
for i in page_title.values():
    search_sug=wikipedia.search(i, suggestion=False)
    for j in search_sug:
        if j==i:
            url_=wikipedia.page(j, auto_suggest=False).url
            urls.append(url_)
print(urls[0:5])
    
 
# parse through html of worrect wikipedia page to get birth information from infobox 

for url in urls:  
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')
    left=soup.find_all("th", class_="infobox-label")
    for left_element in left:
        if left_element.text=="Born":
            datawewant=left_element.find_next_sibling("td").text
            age_data.append(str(datawewant))
        else:
            age_data.append("not found")
            
                
                
                
#now take year from age data
born_year=[]
for i in age_data:
    if i=="none":
        born_year.append("none")
    else:
        year=re.match(r'.*([1-3][0-9]{3})', i).group(1)
        born_year.append(year)





