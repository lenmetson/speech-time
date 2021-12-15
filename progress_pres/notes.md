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

However, the ouput is excessively poulated with "not found" data, as most of the MP's wikipedia pages either do not have infoboxes or do not have data avilable for their birth year.

This is why we will try a different, more systemic approach by querying the wikidata service directly (in python). We are currently getting acquatined with SPARQL, a querying language for data stored using Ressource Description Framework method. One challenge is that it is easy to select data that matches triple property, but not to directly read the date of birth value for a given wikidata page, since this data is not structured. The easy way out is to parse through the html once more,



## Part 2: Findings
### Slide 2.1 
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



## Part 3: Final product ideas (AS)

### Slide 3.1:
