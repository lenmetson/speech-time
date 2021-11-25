# DS105M Presentation Notes

Please find accompanying notes for our presentation here.

## Introduction

This presentation will outline how we are managing our data, some early summary statistics of our data and finally an indication of the next steps for our project.

Some information on our presentation:

* Our presentation is coded in the R Markdown language (.Rmd). You can find the raw code in this repository under the `slides` folder. The file is called `rmdslides.Rmd`. When compiled in RStudio, the file converts the markdown language we have imputed into an HTML file (which you can find in the same folder). This HTML file is what we will view.

* The advantage of this approach is that it allows us to run code live in the markdown which updates each time it is compiled. Any of the summary statistics are code rather than text. This means that if one person makes a change to the data, the related slide does not have to be rewritten.

* If you want to run the presentation on your own machine consult the `README.md` file for the overall repository.

# Part 1: Summary and workflow

## Slide 1.1: Brief summary

Our project is aiming to visualise gender biases in Scottish Parliamentary debates. We know from other contexts that women generally tend to contribute less in professional and legislative settings because of gender discrimination in these environments. Our project aims to quantify and visualise this so as to inform people of the problem.

## Slide 1.2: Organisation

We thought carefully about how to organise our project. Our guiding principle is reproducibility. This is because we want to be fully transparent in our procedures and furthermore we want to make everything we do open-source so that others can improve it in the future. This also has the advantage of others being able to view and check our code so that if there are mistakes, they can be more easily flagged.

We define reproducibility as any user on any machine being able to run our full project using only the materials contained in our GitHub repository. There should be no financial cost to them and they should be able to edit and create their own project without restriction.

Because of this, we needed to make sure that everything we do to the data is programmatically done. For example, we use the HTTPS protocol to download our data in code rather than asking each user to download a copy manually. Furthermore all of our data wrangling is done programmatically so that anyone can get the same results as us simply by running our code.  

## Slide 1.3: Workflow

One challenge in obtaining our data is that we had divided tasks and each of us were using different tools to complete them. This included Atom, Spyder, CSS, RStudio. Therefore, we decided that GitHub would be the best way to ensure that we could all access the latest versions of what others were working on.

No matter what application we were using, we could commit changes either through the application (RStudio, Atom) or through the terminal from our local disk. For example, if Noemie changed something with the way the data is organised, those changes would come up when Len reran the code in our Markdown and Alanah's formatting would also show up.  This meant that we could work effectively on different parts of the project simultaneously.

# Part 2: The Data

## Slide 2.1: Obtaining the data

The raw data for our project is contained on a server managed by Harvard Dataverse. This is an online repository where people can store large datafiles. It is intended for academic purposes. Researchers often upload replication data or datasets for others to use.

We are using the dataset ParlScot. This data is publicly available for free. It consists of scrapped data from Scottish plenary debates. The data is relational and is stored as semi-structured data.

Each row is a single entry in Hansard. The columns represent various meta-data about the speeches such as: the MSP who said it and various information about that MP.

We downloaded the data using the HTTP protocol. The code for this is shown below. It is written in R. The code will work on any machine so long as that machine has cloned our whole repository. Opening `speech-time.Rproj` will launch RStudio with the correct root directory specified. The `here()` function specifies relative paths so it will read files relative to your root directory.

```
install.packages(here)
library(here)
# specify the url
url <- "https://dataverse.harvard.edu/api/access/datafile/4432885"

# download the file into a specified path - add your analysis folder in between " "
download.file(url, here("data_raw", "rawdata.csv"))

```

This will add the raw data to the data_raw directory you can see on the GitHub. However the `.gitignore` file ensured that we didn't push the raw csv into GitHub from our local disks.


## Part 2.2: Summary statistics
The code we ran in for the Markdown is included here:

```
# select name and gender variables from speeches
msps <- speeches %>% select(name, gender)

# retain only unique values (because each MSPs' name is repeated in each speech)
msps <- unique(msps)

# non-MSPs have no gender associated so drop all rows with NA in gender
msps <- drop_na(msps)
```

We also ran some code in python locally (on disk) in parallel to cross check-results. This, among other things, allowed us to realize that we had been using different datasets, and to flag certain inconvenient n/a values in the dataset and drop them to facilitate analysis. The code that follows was first written and executed as it appears to have faster access to the statistics, and later rewritten in python. The switch has been principally motivated by the flexibility that python code offers. In effect, the possibility to define and modulate functions allowed us to obtain summary statistics on any variable present in the dataset and perform some elementary analytics faster. In essence, the marginal cost of using python once some  ad-hoc functions are defined is much lower than for using R. An important note is that this does not affect the reproducibility of the analysis on other machines as the python code can be directly read within R-studio, given the right packages are installed.


## Slide 2.3: Summary statistics on speeches

Number of speeches: `nrow(speeches)`

Number of speeches by women: `nrow(subset(speeches, speeches$gender == "F"))`

Percentage of speeches by women `(nrow(subset(speeches, speeches$gender == "F"))/ nrow(speeches))*100`


## Slide 2.4: Summary statistics on MSPs

We then create a dataframe of MSPs. When the dataset was compiled, the relational table for gender only has values for MSPs. So by dropping all rows of MSPs with no gender, we keep only MSPs

```
# select name and gender variables from speeches
msps <- speeches %>% select(name, gender)

# retain only unique values (because each MSPs' name is repeated in each speech)
msps <- unique(msps)

# non-MSPs have no gender associated so drop all rows with NA in gender
msps <- drop_na(msps)
```

Number of MSPs in our data: `nrow(msps)`

Number of women MSPs in our data: `nrow(subset(msps, msps$gender == "F"))`

Propotion of women MSPs in our data: `(nrow(subset(msps, msps$gender == "F"))/ nrow(msps))*100`

# Part 3 Where next

## Slide 3.1: Data Wrangling

We hope to execute the rest of our analysis in python, because the libraries of interest to us for segmenting the speeches into syllables are easily available in python (notably, the syllables package or the cmudict library instead which is slower but more accurate). With this in mind, we reiterated the data cleaning process in python and performed some further exploratory analysis, which I will give an overview of here, with an emphasis on the challenges that we have faced with the data. 

The first step in the analysis is cleaning the data. Firstly, we neededdiscard any speeches related to formalities, and introductory speeches that have procedural relevance but would not inform our analysis. The challenge was to automate the decision of which text was a proper speech and which was not. Thankfully, there was a very useful variable in the data that classified the texts according to whether they were speeches as 1 or 0. The next natural step is to drop all the rows that contained a 0 in the "is_speech" column, in other words subsetting the original table to create a table that only contains data where the text is a proper speech. We did this with the following code:

```
import pandas as pd
import numpy as np

#upload data from disk into a pandas dataframe
print('-----------------------------------------------------------------')
print("Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.")
print('-----------------------------------------------------------------')


harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

#create dataframe with only rows where there is a speech, using boolean indexing, discarding intro phrases and such.

speech_table=harvard[:][harvard["is_speech"]==1]

#create a list with the column names called header
header=[]
for column in speech_table.columns:
  header.append(column)

#slice df to obtain first 2 rows
view_table=speech_table.iloc[0:2, :]


print('-----------------------------------------------------------------')
print("showing header and first 2 rows of obtained dataframe called speech_table, as well as some important statistics.")
print('-----------------------------------------------------------------')

print(view_table)
print(header)
```

We get the following results:
```
-----------------------------------------------------------------
Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.
-----------------------------------------------------------------
-----------------------------------------------------------------
showing header and first 2 rows of obtained dataframe called speech_table, as well as some important statistics.
-----------------------------------------------------------------
   Unnamed: 0  x  daily_order_no  ...      msp_type  wikidataid party.facts.id
2           3  3               3  ...        Region     Q334015          986.0
5           6  6               6  ...  Constituency      Q10652          986.0

[2 rows x 21 columns]
['Unnamed: 0', 'x', 'daily_order_no', 'order_no', 'is_speech', 'committee', 'date', 'item', 'type', 'office_held', 'display_as', 'name', 'speech', 'parl_id', 'party', 'gender', 'constituency', 'region', 'msp_type', 'wikidataid', 'party.facts.id']

```
To get the total number of speeches, we can simply then count the rows. But ideally we wanted to avoid repeating this process to get the dimensions of all the table subsets we will be creating, so we created the following function and used it on the table with only speeches:

```
def get_shape(dataset):
  shape=dataset.shape
  return ("The dimensions of this data is {}".format(shape))

#get number of speeches
number_speeches=get_shape(speech_table)[0]
print('The total number of speeches is: {}.'.format(number_speeches))
```

The second step, again in this reproducibility philosophy was to define some useful functions for exploratory analysis. Namely, we developed two functions that solved two problems. Firstly, to find information on MPs, such as the total number of men, of women, or the total number of constituencies represented as opposed to regions represented, the problem was that these vaues were repeated in the dataset because each MP speaks more than once and their speeches are recorded in separate rows. So we defined a function to extract these stats essentially by using boolean indexing:
```
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
```

Here are some applications of this funciton: we can easily get the total number and names of women, men, constituencies, regions. I also included a sort of filter in the function so it could easily return, for example, the all women who represented a constituency. This saves a lot of time and renders data exploration quite accessible and modulable.
```
#get lists of unique values of the following data:

names_women=find_unique_values(speech_table, "name", feature1="gender", feature2="F", comment=True, dictionary=False)
print(names_women)

names_men=find_unique_values(speech_table, "name", feature1="gender", feature2="M", comment=True, dictionary=False)
print(names_men)

constituencies_women=find_unique_values(speech_table, "constituency", "gender", "F", True, False)
print(constituencies_women)

constituencies_men=find_unique_values(speech_table, "constituency", "gender", "M", True, False)
print(constituencies_women)

regions_women=find_unique_values(speech_table, "region", "gender", "F", True, False)
print(regions_women)

regions_men=find_unique_values(speech_table, "region", "gender", "F", True, False)
print(regions_men)
```

The second problem was that we wanted to get a sense of perhaps some discrimination in parliament. We saw there was a daily order number variable, which we thought represented the order in which MSPs speak in parliament. But to do this we could not ue the same funciton, as these daily orders are repeated over the dataset since the data runs over a few years. So we created a different function:

```
#define function to get values in column
def find_values(dataset, column, feature1, feature2, comment=True):
    if feature1!="none":
        dataset=dataset[dataset[feature1]==feature2]
    values=dataset[column]
    if comment==True:
        print("The {} with the following filter: {} is {} are given below.".format(column, feature1, feature2))
    return values
 ```
 
Using this one, we saw that contrary to our initial thoughts on the average and median order number was higher for women than men.
```
women_daily_order=find_values(speech_table, "daily_order_no", "gender", "F", True)
print(women_daily_order)
print("The average daily order for women is:")
women_daily_order_avg=women_daily_order.mean()
print(women_daily_order_avg)

men_daily_order=find_values(speech_table, "daily_order_no", "gender", "M", True)
print(men_daily_order)
print("The average daily order for men is:")
men_daily_order_avg=men_daily_order.mean()
print(men_daily_order_avg)

print("The median daily order for women is:")
women_daily_order_med=women_daily_order.median()
print(women_daily_order_med)

print("The median daily order for men is:")
men_daily_order_med=men_daily_order.median()
print(men_daily_order_med)
```

It is worth noting that the two functions I mentioned return series of values, which are pandas objects so I also defined a third on to count the number of values returned. This is just a tengential note:

```
def number_unique_values(list_unique_values):
  totals=[]
  for value in list_unique_values:
    number=len(value)
    totals.append(number)
  return totals
  ```


The second step in prepping our data was stripping it of n/a values. More specifically, we wanted to ensure overall accuracy within the data. For example, we noticed some MPs had no gender classifications. There had N/A values in the gender column. This is because they were either experts, or on-off interventions on specific subjects. As the final project we have in mind has a higher-level objective of studying gender discrimination among MSPs, we created a table with information on MPs. We droped duplicate rows and dropped rows where the "parl_id" and "gender" columns contained N/A values. This is pretty simple code, and yields clean data where all speakers are MSPs and their gender and type (constituency or region) is recorded:

```
#create a dataframe with the unique MP names and their respective information, but discarding speeches.
mp_speeches=speech_table.dropna(axis=0,how='any', subset=["parl_id", "gender", "msp_type"])
```

With this data_table, we can easily extract the corresponding names of constituency and region, which we will later use relationally with a table that contains the polar coordinates of these geographical areas to create a heat map on Tableau. We can also be confident that the text data we will analyse is reliablly speech text and can be classified along heuristics of gender and constituency/region.

The main data source for analysis is now ready to be used. We can now use some partitions of this dataframe to count the number of syllables spoken by MSPs and compare the obtained values between men and women.



## Slide 3.2: Analysis

As we already know how to operationalize pre-existing libraries for syllable count, here are some insights we would like to draw from the data:
- average and median number of syllables by gender
- whether this discrepency also exists on Twitter
- perform some sentiment analysis on speeches to see if a gender-related lexic is found at a higher rate in women's speeches than in men's speeches.

## Slide 3.3: Visualisations planned

Our process thus far has been continually informed by our plans for the final product: various data visualisations of the gender differences in Scottish parliamentary contributions. We've done this by not only by ensuring that we're able to obtain the relevant data and insights for our product, but also by cross-checking that our data format is suitable for the program we are planning to use for the data visualiations (namely, Tableau Public).

| What we're planning to visualise                                                                                   | Graph                           | Variables                                                      |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------|----------------------------------------------------------------|
| Change in gender differences of speech time over the years                                                        | Stacked column graph            | gender (m/f, columns), speech time (%, y axis), years (x axis) |
| Power in parliament represented by amount of seats taken up once gender differences in speech time are considered | Scottish parliamentary seat map | gender (m/f), speech time (%)                                  |
| Relationship between speech time and age                                                                          | Scatter graph                   | gender (m/f), speech time (n)                                  |
| Absolute gender differences in amount of speech                                                                   | Speech bubbles                  | gender (m/f), speech time (%)                                  |
| Proportions of time men and women speak                                                                           | Circle chart                    | gender (m/f), speech time (%)                                  |
| Party comparison of women speech time                                                                             | Stacked bar chart               | gender (m/f, bars), MP political party (y axis),               |
| Comparison of Twitter activity and speech time                                                                    | Line graph                      | speech time (n, y axis), Twitter followers (n, x axis)         |
| Regional differences in gender speech times                                                                    | Heat map                      | speech time (%), gender (m/f)         |

Tableau Public is a free platform that can connect to data in a variety of formats like Excel, CSV, and JSON, as well as being able to connect to a server. We've chosen Tableau as a data visualisation tool as it can take in data and produce the required data visualisation output in a short time. We are planning on using a CSV Web Data Connector to connect Tableau directly to the CSV in our GitHub repository. This means that any changes in the data should automatically update the visualisations.
