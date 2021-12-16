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

#get wikipage title from wikiID
  
    
age_data={}

for wikiId in wiki:
    url="https://www.wikidata.org/wiki/{}".format(wikiId)
    r=requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    row = soup.find("div", {"id":"P569"})
    if row is not None:
        text=row.find('div', {"class": "wikibase-snakview-value wikibase-snakview-variation-valuesnak"})
        age_data[wikiId]=text.text
    else:
        age_data[wikiId]='none'

age_data['Q334015']="10 July 1929"

born_year=[]
for i in age_data.values:
    if i=="none":
        born_year.append("none")
    else:
        year_draft=re.match(r'.*([1-3][0-9]{3})', i)
        if year_draft is not None:
            year=year_draft.group(3)
            born_year.append(year)  
        else:
            born_year.append("none")
            
wikiId_year={}
j=0
for wikiId in wiki:
    wikiId_year[wikiId]=born_year[j]
    j+=1
    
for i in wikiId_year:
    if wikiId_year[i]=="none":
        print(i) 
        
wikiId_year['Q1258767']="1951"
wikiId_year['Q24034376']="1978"
wikiId_year['Q24039900']="1946"

#others data just not available - Good job on privacy, msps

agedata=pd.DataFrame(wikiId_year.items(), columns=["wikidata ID", "born year"])


