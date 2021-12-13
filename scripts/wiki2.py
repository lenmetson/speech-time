
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup



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
  
    
page_title={}

for wikiId in wiki:
    url="https://www.wikidata.org/w/api.php?action=wbgetentities&format=xml&props=sitelinks&ids={}&sitefilter=enwiki".format(wikiId)
    r=requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.sitelink["title"]
    page_title[wikiId]=result
print(page_title)
