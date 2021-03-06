
import pandas as pd
import numpy as np

#upload data from disk into a pandas dataframe
print('-----------------------------------------------------------------')
print("Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.")
print('-----------------------------------------------------------------')


harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

#create dataframe with only rows where there is a speech, using boolean indexing, discarding intro phrases and such.

speech_table=harvard[:][harvard["is_speech"]==1]

#save the table as a pickle and view itby printing output
speech_table.to_pickle("/Users/noemieclaret/Downloads/speech_table.pkl")
output=pd.read_pickle("/Users/noemieclaret/Downloads/speech_table.pkl")

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

#dowload file as csv to disk if necessary
#speech_table.to_csv('/Users/noemieclaret/Downloads/harvard_speeches.csv')
#noémie note: to_csv is a pandas function!! not built in

def get_shape(dataset):
  shape=dataset.shape
  return ("The dimensions of this data is {}".format(shape))

#get number of speeches
number_speeches=get_shape(speech_table)[0]
print('The total number of speeches is: {}.'.format(number_speeches))

#make a function to return number of unique variables and dictionary containing these values.
#the feature attribute is used as a filter. for exemple, it can be feature=speech_table["gender"]==F.
#if no feature, write feature="none"
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

#define function to get values in column
def find_values(dataset, column, feature1, feature2, comment=True):
    if feature1!="none":
        dataset=dataset[dataset[feature1]==feature2]
    values=dataset[column]
    if comment==True:
        print("The {} with the following filter: {} is {} are given below.".format(column, feature1, feature2))
    return values
  
#define a function to find the number of unique values  
def number_unique_values(list_unique_values):
  totals=[]
  for value in list_unique_values:
    number=len(value)
    totals.append(number)
  return totals

#get lists of unique values of the following relational data:

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
      
      


#how many: women and men, constituencies represented respectively by women and men, regions, msp_type

numbers=number_unique_values([names_women, names_men, constituencies_women, constituencies_men])
print("The number of women and men, constituencies represented respectively by women and men are: {}.".format(numbers))

          
#create a dataframe with the unique MP names and their respective information, but discarding speeches.
mp_info=speech_table.drop_duplicates(subset="name", keep="first").dropna(axis=0,how='any', subset=["parl_id"])

#create dataframe with MPs and their wikiID
mp_wikiID=mp_info["wikidataid"]

print(mp_info.head(3))
print(mp_wikiID.head(3))



