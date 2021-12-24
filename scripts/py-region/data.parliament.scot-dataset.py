#Converting JSON of MSP region to CSV
import json
import pandas as pd

df = pd.read_json('MemberElectionRegionStatuRepository.json')
print(df)


df.to_csv(r'C:\Users\alanahsarginson\Sheet1.csv')
