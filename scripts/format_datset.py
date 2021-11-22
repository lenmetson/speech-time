import pandas as pd

#upload data from disk into a pandas dataframe
#harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')

#create dataframe with only rows where there is a speech

#table only speches
speech_table=harvard[:][harvard["is_speech"]==1]
view_table=speech_table.iloc[0:2, :]
print(view_table)

#dowload file as csv
speech_table.to_csv('/Users/noemieclaret/Downloads/harvard_speeches.csv')


def get_shape:
  shape=dataset.shape
  return ("The shape of this data is {}".format(shape))

#make a series with unique names 
def find_unique_values(dataset, index):
  unique_values=dataset['value'].unique()
  print(unique_values)
    duplicate_attribute=[]
    unique_attribute_byrow={}
    duplicate_attribute_byrow={}
    row_number=0
    
    for row in dataset:
        row_number+=1
        attribute=row[index]
        if attribute in unique_attribute:
            duplicate_attribute.append(attribute)
            duplicate_attribute_byrow[row_number]=attribute
        else:
            unique_attribute.append(attribute)
            unique_attribute_byrow[row_number]=attribute
    number_unique_attributes=len(unique_attribute_byrow)
    number_duplicate_attributes=len(duplicate_attribute_byrow)
    return ("The number of repeated", str(header[index]), "in", dataset_name, "is", number_duplicate_attributes), ("The number of unique", str(header[index]), "in", dataset_name, "is", number_unique_attributes) 
        
 
#make a function to explore this nex datatable
def get_value_byname(dataset=speech_table, value="wikidataid"):
    name_wiki=dataset[["name", "value"]]
    speech_count=speech_name.count()
    print(speech_count)
    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
