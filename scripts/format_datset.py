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

#make a function to return number of unique names and dictionary containing the names.
def find_unique_values(dataset, column, comment=TRUE):
  unique_values=dataset[column].unique() #number of unique values
  val_dict= {idx:column for idx, column in enumerate(dataset[value].unique())} 
  #first, define a funciton to find unique values in a specified column.
  if comment==True:
    print(("The number of {} is {}".format(column, unique_values)),("here is a dictionary with unique values:{}".format(val_dict))
  return [unique values, val_dict]#return both number of unique values and the dictrionary containing them

find_unique_names=(speech_table, "name", comments=TRUE)

#aim: create a dataframe with the unique MP names and their respective information, but discarding speeches.
#create a sereis with just the names of the MPS
mp_names_list=np.array[]
for name in find_unique_names[1]:
          mp_names.append(name[1])
mp_names_series=pd.series(mp_names_list)
          

names_speakers=find_unique_values(speech_table, "name")
print(names_speakers)


#make a pandas dataframe with speaker name and wiki_id
name_wikiid=pd.speech_table["name", "wikidataid"][speech_table["name"]==enumerate(speech_table["name"].unique())]

