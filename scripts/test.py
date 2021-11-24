import pandas as pd
harvard1=pd.read_csv(r/harvard)
speech_table=harvard1[:][harvard1["is_speech"]==1]
