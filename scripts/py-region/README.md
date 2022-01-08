# IGNORE REPOSITORY - WAS TRAINING EXERCISE

The purpose of the exercises in this folder is for Alanah to try to obtain a CSV with all MSPs across every parliamentary session, their gender, and the region they represent to practice using python.

This was done using python up until obtaining two CSVs: one containing MSP names and gender, and the other containing their regions. The PersonID dimension linked them both. However, they weren't identical; one CSV had more rows than the other, so we had to filter one CSV's range of PersonIDs agianst the other. There was trouble doing this, for example with codes such as:
```
import pandas as pd
import csv

with open(r'LIST TO COMPARE.csv') as f:
    reader = csv.reader(f)
    data = list(reader)


data2 = pd.read_csv(r'Sheet2.csv')

nf = csv.writer(open("output.csv", "w"))
with open(r'Sheet2.csv', 'rb') as g:
    reader1 = csv.reader(g)
    for row in reader1:
        if(''.join(row) in list):
            nf.writerow([''.join(row),1])
        else:
            nf.writerow([''.join(row),0])
  ```
  
  and
  
  ```
import pandas as pd

# reading two csv files
data1 = pd.read_csv(r'Sheet1.csv')
data2 = pd.read_csv(r'Sheet2.csv')

# using merge function by setting how='inner'
df = pd.merge(data1, data2,
				on='PersonID',
				how='inner')

# displaying result
print(df)
  ```
  
 ...but we couldn't get either to work.
 
 We therefore edited the CSVs directly on a local machine, using Excel filtering functions to eventually compile both CSVs into one list (as seen in the output.data folder).
