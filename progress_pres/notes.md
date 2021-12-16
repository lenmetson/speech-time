# DS105M Second Presentation Notes
Please find the accompanying notes for our presentation here.

## Introduction
This presentation will discuss the analysis of our data and the ideas we have for our final product.

Some information on our presentation:


## Part 1: Analysis

### Slide 1.1: Data wrangling

Problems with data:
* Asymmetric duplication in the speeches.
* Speeches doubled but order no. a running variable.
* This meant that we had to reshape the data so as to remove duplicated speeches

### Slide 1.2: Gender and speeches
#### 1.2.1 Gender and syllables
The `sylcounts` packages returns and estimate of the number of syllables in a vector of words. However, the output is a vector. For example, the output for the sentence `"I disagree with you"` would have the output `c(1, 3, 1, 1)`. However, we need an estimate the sum of syllables in a speech. I used the `lapply` function to sum the vectors for each speech.

*Include image*

#### 1.2.2 Gender and content

The basis of our analysis is that this question is important because women being able to speak in legislative settings means women will be more represented. This claim gets complex when we get into the political science of representation and especially representation based on group characteristics. Further, better specified analysis would be needed to test this assumption legitimately. However, just for illustration purposes we did a very basic dictionary content analysis to see if female MSPs did talk more about women.

This was done using string matching. First we cleaned the data by making it all lower case and removing punctuation marks. We then applied a string matching function using the library `stringr` which returned a numeric binary for whether a match was found:

```
gen_dict <- "woman*|women*|female*|femin*|sexism"
speeches$about_gen <-  as.integer(str_detect(speeches$speech, gen_dict))
```




### Slide 1.3: More variables: Wiki API

To see if we can extract any meaningful insight relating speech time and womens' age, we need to find the date of birth for all MSPs in our data.
We have tries multiple approaches for this. First, we used the web-scraping approach to obtain birth date data (which can have many forms, i.e strings, year, tuple) from the xikipedia infoboxes. 

For this, we first created a list with all distinct wikidata ID present in ot dataset. 

```

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

```
We then iterated through this list to and made an https request (using the python requests library) to the wikidata API to get the correspinding page title for each wikidata ID. This is incorporated in the request by using the string formatting method embedded in the hardcoded url.
SPARQL= query language to retrieve data stored in RDF (ressource description framework) format. We parse through the resulting html using BeautifulSoup to get the page title, and appended this to a dictionary.

```
 #get wikipage title from wikiID
  
    
page_title={}

for wikiId in wiki:
    url="https://www.wikidata.org/w/api.php?action=wbgetentities&format=xml&props=sitelinks&ids={}&sitefilter=enwiki".format(wikiId)
    r=requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.sitelink["title"]
    page_title[wikiId]=result
    
```

We then used the python wikipedia library with the search, page and url modules to iterate though page suggestions, find the one that corresponded to the right MSP and get the corresponding url.
```
age_data=[]

urls=[]
for i in page_title.values():
    search_sug=wikipedia.search(i, suggestion=False)
    for j in search_sug:
        if j==i:
            url_=wikipedia.page(j, auto_suggest=False).url
            urls.append(url_)
print(urls[0:5])
```
Now that we have the correct urls, we can parse through the infobox HTML and get the information corresponding to the "born" row. But if there is no such row, we ask the algorithm to add "not found" to the list of date of borth information.


```
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
```
And finally, we extract the year from the "born" data where it is available using the re library.

```
born_year=[]
for i in age_data:
    if i=="none":
        born_year.append("none")
    else:
        year=re.match(r'.*([1-3][0-9]{3})', i).group(1)
        born_year.append(year)

```

However, the ouput is excessively poulated with "not found" data, as most of the MP's wikipedia pages either do not have infoboxes or do not have data avilable for their birth year.(1)



This is why we also trid a different, more systemic approach by querying the wikidata service directly. This entailed learning SPARQL, a querying language for data stored using Ressource Description Framework method. One challenge is that it is easy to select data that matches triple property, but not to directly read the date of birth value for a given wikidata page, since this data is not structured. The easy way out is to parse through the html once more. This is what we did - amending some of the code we wrote earlier, we use request to get to the MSP's wikidata page instead and parse through the html to obtain a string with an exact date of bbirth, and then use the re library to extract only the year.

As written in the code, if the relevant html can't be found, or if there is no year within this data (in effect, in a few wikidata pages, only "Born in the 20th century" appreared. For these 5 or 6 cases, we reasearched the MSPs' names and added their age manully. Some just do not have their age available, so we will just exclude these from analysis without too luch loss of statistical accuracy since these are only one of two MSPs.

```
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
        
(2)

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
(3)
            
wikiId_year={}
j=0
for wikiId in wiki:
    wikiId_year[wikiId]=born_year[j]
    j+=1


(4)


for i in wikiId_year:
    if wikiId_year[i]=="none":
        print(i) 
        
        
(5)
        
wikiId_year['Q1258767']="1951"
wikiId_year['Q24034376']="1978"
wikiId_year['Q24039900']="1946"

#others data just not available - Good job on privacy, msps

agedata=pd.DataFrame(wikiId_year.items(), columns=["wikidata ID", "born year"])

(6)


```






### Slide 2.2
### Slide 2.3 Gender and gender focus

* %speeches by men about women: *2.32%*
* %speeches by women about women: *5.48%*
```

                    ─────────────────────────
(Intercept)                          0.05 ***  
                                    (0.00)     
genderM                             -0.03 ***  
                                    (0.00)     
                    ─────────────────────────
N                                   390586         
R2                                   0.01      
─────────────────────────────────────────────
*** p < 0.001; ** p < 0.01; * p < 0.05.        

```

### Slide 2.1: More detailed background
There have been six elections to the Scottish Parliament: 1999, 2003, 2007, 2011, 2016 and 2021. Thus there have only been 5 parliaments so far.

| Parliament              | Election Date | Dissolution Date |
|-------------------------|---------------|------------------|
| 1st Scottish Parliament | 12-05-1999    | 31-03-2003       |
| 2nd Scottish Parliament | 07-05-2003    | 02-04-2007       |
| 3rd Scottish Parliament | 14-05-2007    | 22-03-2011       |
| 4th Scottish Parliament | 11-05-2011    | 24-03-2016       |
| 5th Scottish Parliament | 12-05-2016    | 05-05-2021       |
| 6th Scottish Parliament | 13-05-2021    | NA               |



## Part 3: Final product progress

### Slide 3.1: Loading summary statistics data
* We now have data we can work with in the 'speech-timeoutput_data' folder in our Github repository
* This includes the '.csv' file 'summary_year.csv', that included yearly, gender-separated data on:
    * Number of MSPs who spoke
    * Number of syllables spoken
    * Number of speeches
    * Proportion of women-focused speeches
* We decided on separating the data on years rather than parliaments so as to provide a continuous axis in the product rather than discrete
* This way, we can introduce the discrete dimension of parliamentary sessions as marks on the visualisation
* This data was then downloaded on a local machine, to be connected to in Tableau Public as a text file

### Slide 3.2: Loading summary data + dimensions and measures
(insert Screenshot 2021-12-16 at 01.12.07) + (insert Screenshot 2021-12-16 at 01.07.52)
* Once we connected the file, dragged the sheet to the workspace and created the relevant worksheet, a problem had quickly been made apparent in how we had labelled our data
* We had differentiated gender via the columns, instead of inputting them as discrete values in rows in a specific gender-dimension column
(insert Screenshot 2021-12-16 at 01.07.52)
* What this had meant is that gender wasn't recognised as a dimension holding two discrete values (men/women)
* The solution to this problem was creating a way to successfully separate years and gender as dimensions
* We decided to stick to making changes to the '.csv' on the local machine, before translating the changes to the R code that produced the output data and its respective columns/rows

(insert Screenshot 2021-12-16 at 01.21.34)
* As such, we created a new column - 'Gender' - and separated the values between this new dimension
* This created two rows for each year - one for men, and one for women
(insert Screenshot 2021-12-16 at 01.05.10)
* The result was a much tidier table in Tableau, translating to an easier and more efficient way of exploring and visualising the data through its better-defined dimensions and measures

### Slide 3.3: Building the visualisation - example
The first visualisation looked at the changes in gender differences of speech time over the years. We planned to represent data on syllable count using a stacked column graph.
1. We first set our column as our years
2. We then set our rows as the sum number of syllables spoken each year
3. We next wanted to visually differentiate how the genders differ in this measure, so did so by attributing gender to a colour mark, editing the colourway to represent more 'gender-representative colours'
We believed the stacked bar chart best represented two elements of our investigation:
1. The dominance men have in speaking in parliament over the years
2. The changing picture as women are speaking more in parliament 
(insert Screenshot 2021-12-16 at 01.27.13)

### Slide 3.4: Building the dashboard
* We anticipate the final product as a centralised dashboard hosting:
    * All of the different visualisations
    * Text detailing our aim, process, results and conclusions, as well as our header and an overview of the project
    * Links to the data sources that we have used
* Here is the rough visual layout that was proposed at the start of the project:
(insert Screenshot 2021-12-16 at 01.40.42)
* Here is an example using two initial visualisations so far of how such the dashboard would function on Tableau
(insert Screenshot 2021-12-16 at 01.37.21)

### Slide 3.5: Next steps
#### Slide 3.5.1: Segmenting by term
* One key step will be segmenting by term
    * One way to do this could be to edit the '.csv' directly and create a separate column called 'Parliamentary session', and using the table in Slide 2.1 to label the rows accordingly. This would then create a discrete dimension which would be applied to visualisations
    * Another potential way to do this is by using the 'Filter' function to filter the visualisations by certain time-frames - although this avenue hasn't been fully explored yet

#### Slide 3.5.2: Applying visual best practices
* Another important step is applying visual best practices to tell the story: this is an exciting opportunity to conduct independent research and explore how the data viz. community are presenting their data
* This will be of a particular challenge for visualisations whose graphs are non-conventional, for example using the Scottish parliamentary seat map to show the power in parliament by amount of seats taken up once gender differences in speech time are considered

#### Slide 3.5.3: Interactive opportunities
* Lastly, we'll be building interactive elements into the dashboard by using filters to allow the user to explore tha data themselves
* Returning to the table from our previous presentation, a learning so far has been the importance of being clear on what specific data is needed and how it needs to be presented to communicate the intended message, so that the process of extracting, cleaning, exporting, connecting, and ultimately visualising the data is streamlined
