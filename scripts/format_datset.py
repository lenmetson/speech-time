import pandas as pd

#upload data from disk into a pandas dataframe
harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

#create dataframe with only rows where there is a speech

#table only speches
speech_table=harvard[:][harvard["is_speech"]==1]
view_table=speech_table.iloc[0:2, :]
print(view_table)

#dowload file as csv
speech_table.to_csv('/Users/noemieclaret/Downloads/harvard_speeches.csv')


def get_shape(dataset):
  shape=dataset.shape
  return ("The shape of this data is {}".format(shape))

#make a dictionary with unique names 
def find_unique_values(dataset, value):
  unique_values=dataset[value].unique()
  val_dict= {idx:value for idx , value in enumerate(dataset[value].unique())}
  return ("The number of values is {}".format( unique_values)),("here is a dictionary with the values:{}".format( val_dict))

names_speakers=find_unique_values(speech_table, "name")
print(names_speakers)


#make a pandas dataframe with speaker name and wiki_id
name_wikiid=pd.speech_table["name", "wikidataid"][speech_table["name"]==enumerate(speech_table["name"].unique())]

