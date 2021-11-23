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
for column in data.columns:
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
print(f'The total number of speeches is: {}.'.format(number_speeches))

#make a function to return number of unique variables and dictionary containing these values.
#the feature attribute is used as a filter. for exemple, it can be feature=speech_table["gender"]==F.
#if no feature, write feature=none
def find_unique_values(dataset, column, feature, comment=TRUE):
  if feature!=none:
    dataset=datset.loc[:,feature]
  unique_values=dataset[column].unique() #number of unique values
  val_dict= {idx:column for idx, column in enumerate(dataset[value].unique())} 
  if comment==True:
    print(("The number of {} is {}".format(column, unique_values)),("here is a dictionary with unique values:{}".format(val_dict))
  return [unique values, val_dict]#return both number of unique values and the dictrionary containing them

find_unique_names=(speech_table, "name", comments=TRUE)
         
          
#find out how many women in total
women_number=find_unique_values(speech_table, column="name", feature=speech_table["gener"]=="F", comment=False)
print(women_number)

          
#how many men
men_number=find_unique_values(speech_table, column="name", feature=none, comment=False)[0]-women_number
          
          
#create a dataframe with the unique MP names and their respective information, but discarding speeches.
mp_info=speech_table.drop_duplicates(subset="name", keep="first")   
          
#how many constituencies 
constituency_number=find_unique_values(mp_info , column="?", feature=mp_info["constituency?olumn?"]=="constituency?"],comment=True)         
          
         
          
          
#make a pandas dataframe with speaker name and wiki_id
name_wikiid=pd.speech_table["name", "wikidataid"][speech_table["name"]==enumerate(speech_table["name"].unique())]

