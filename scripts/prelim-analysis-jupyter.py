## First import useful libraries then put data into pandas dataframe


import pandas as pd

## Upload data from disk and convert csv to pandas DataFrame

print('-----------------------------------------------------------------')
print("Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.")
print('-----------------------------------------------------------------')


harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

## Subset table where the speeches are actually speeches

speech_table=harvard[:][harvard["is_speech"]==1]


## Print table to view


speeches=speech_table["speech"]
print(speeches)


## Get rid of the rows where the speaker does not have a gender or parl_id

speech_table_gender_parlID=speech_table[:][speech_table["gender"]==("F" or "M")].dropna(axis=0, how='any', subset=["type"])
speeches_2=speech_table_gender_parlID[["name", "speech"]]
print(speeches_2)
print(type(speeches_2))



# Look at the different types of items 
(Is there a special category for procedural speeches? seems like it might be oaths and affirmations)


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



# Look at which speakers have spoken for oaths and affirmations. 
Can we take them out wihtout loss of insight on man/woman speaking ratio? Does not seem judicious. 

oaths_aff_speakers=find_values(speech_table, "name", "item", "Oaths and Affirmations", True)
print(oaths_aff_speakers)

# See proportion of women to men for oaths and affirmations

def find_unique_values_bis(dataset, column, feature1, feature2, feature3, feature4, comment=True):
    if feature1!="none" and feature3!="none":
        dataset=dataset[dataset[feature1]==feature2][dataset[feature3]==feature4]
    values=dataset[column].unique()
    if comment==True:
        print("The {} with the following filter: {} is {} are given below.".format(column, feature1, feature2))
    return values

women_names_oath_aff=find_unique_values_bis(speech_table, "name", "item", "Oaths and Affirmations", "gender", "F", False)
print(len(women_names_oath_aff))


So in total there are 211 people who spoke in oaths and affirmations and 51 of these were women. This is up to interpretation. We need to see if this ratio corresponds to the gender distribution in parliament, and decide if we deem a higher/lower proportion of women who speak only of procedural matters a good thing. 

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

