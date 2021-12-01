
```python
import pandas as pd

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

```

#create a list with the column names called header
header=[]
for column in speech_table.columns:
  header.append(column)

#get dimensions of dataset
def get_shape(dataset):
  shape=dataset.shape
  return ("The dimensions of this data is {}".format(shape))

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

#create a dataframe with the unique MP names and their respective information, but discarding speeches.
mp_info=speech_table.drop_duplicates(subset="name", keep="first").dropna(axis=0,how='any', subset=["parl_id"])

#create dataframe with MPs and their wikiID
mp_wikiID=mp_info["wikidataid"]

print(mp_info.head(3))
print(mp_wikiID.head(3))





























