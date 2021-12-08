## First import useful libraries then put data into pandas dataframe

import numpy as np
import pandas as pd

## Upload data from disk and convert csv to pandas DataFrame

# LM: I will have a look at a way to set relative file paths in python
harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

## Subset table where the speeches are actually speeches

speech_table=harvard[:][harvard["is_speech"]==1]


## Get rid of the rows where the speaker does not have a gender or parl_id

speech_table_gender_parlID=speech_table[:][speech_table["gender"]==("F" or "M")].dropna(axis=0, how='any', subset=["type"])
# LM: can we do this by dropping just those without parl_id, that feels more legit given it's our justification?


# Look at the different types of items
#(Is there a special category for procedural speeches? seems like it might be oaths and affirmations)


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
items=find_unique_values(speech_table, "item", "none", "none", True, False)
print(items)


def find_values(dataset, column, feature1, feature2, comment=True):
    if feature1!="none":
        dataset=dataset[dataset[feature1]==feature2]
    values=dataset[column]
    if comment==True:
        print("The {} with the following filter: {} is {} are given below.".format(column, feature1, feature2))
    return values

# Create a new column in speech_table with the word count of each speech

speech_table["speech_word_count"]=speech_table["speech"].str.count(' ')+1

# Find the total number of words for women and men and find ratio

total_words_women_series=find_values(speech_table, "speech_word_count", "gender", "F", False)
total_words_women=sum(total_words_women_series)
print(total_words_women)

total_words_men_series=find_values(speech_table, "speech_word_count", "gender", "M", False)
total_words_men=sum(total_words_men_series)
print(total_words_men)

print(total_words_women/total_words_men)

# Create a dictionary with the propotion of women words to men words indexed by year

#first create a dictionary with the years (seems useless but just to check we are acutally getting years where things happened)


dates=find_unique_values(speech_table, "date", "none", "none", False)
print(dates)

years=[]
for date in dates:
    year=date[0:4]
    if year not in years:
        years.append(year)
    else:
        continue
print(years)


# define a function to find values in a column with two filters

def find_values_bis(dataset, column, feature1, feature2, feature3, feature4,comment=True):
    if feature1!="none":
        dataset=dataset[dataset[feature1]==feature2][dataset[feature3]==feature4]
    values=dataset[column]
    if comment==True:
        print("The {} with the following filter: {} is {} are given below.".format(column, feature1, feature2))
    return values

#Now get the proportion of words spoken by women to men each year

#get new column with year

speech_table["year"]=speech_table["date"].str[0:4]
print(speech_table["year"])

year_words_women=[]
for year in years:
    total_words_women_series=find_values_bis(speech_table, "speech_word_count", "gender", "F","year", year, False)
    total_words_women=sum(total_words_women_series)
    year_words_women.append(total_words_women)

freq_table_words_women_byyear=pd.DataFrame({"years":years, "words":year_words_women})
print(freq_table_words_women_byyear)


year_words_men=[]
for year in years:
    total_words_men_series=find_values_bis(speech_table, "speech_word_count", "gender", "M","year", year, False)
    total_words_men=sum(total_words_men_series)
    year_words_men.append(total_words_men)

freq_table_words_men_byyear=pd.DataFrame({"years":years, "words":year_words_men})
print(freq_table_words_women_byyear)

data={"years":years, "words_ratio":np.array(year_words_women)/np.array(year_words_men)}
ratio_words_gender_byyear=pd.DataFrame(data)
print(ratio_words_gender_byyear)

# But these results may not mean much
# We need to use the proportion of women to men each year and see if the increase in words spoken is just due to the increase in the number of women


number_women_year=[]
for year in years:
    number_women_series=find_unique_values_bis(speech_table, "name", "gender", "F","year", year, False)
    number_women=len(number_women_series)
    number_women_year.append(number_women)
print(number_women_year)

number_men_year=[]
for year in years:
    number_men_series=find_unique_values_bis(speech_table, "name", "gender", "M","year", year, False)
    number_men=len(number_men_series)
    number_men_year.append(number_men)
print(number_men_year)

ratio_words_gender_byyear["ratio_women_men"]=np.array(number_women_year)/np.array(number_men_year)
ratio_words_gender_byyear["words_spoken_to_gender_distribution"]=ratio_words_gender_byyear["words_ratio"]/ratio_words_gender_byyear["ratio_women_men"]

print(ratio_words_gender_byyear)

#download to json format
ratio_words_gender_byyear.to_json(path_or_buf=="speech-time/data_raw")

# Plot for visualization

import matplotlib.pyplot as plt
plt.plot(ratio_words_gender_byyear["years"],ratio_words_gender_byyear["words_spoken_to_gender_distribution"])
