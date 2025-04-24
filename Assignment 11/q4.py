import pandas as pd
import numpy as np
name={'Day':range(1,4), 'John':['True','False','True'],'Kavin':['True','False','False']}
df=pd.DataFrame(name)

def is_party(row):
    return row['John'] and row['Kavin']
df['party']=df.apply(is_party,axis=1)

df['days_til_party']=-1

days=float('inf')
for i in range(len(df)-1,-1,-1):
    if df.loc[i,'party']:
        days=0
        df.loc[i,'days_til_party']=0
    else:
        if days!=float('inf'):
            days+=1
            df.loc[i,'days_til_party']=days
        else:
            df.loc[i,'days_til_party']=float('inf')

df['days_til_party']=df['days_til_party'].replace(float('inf'),-1)
print(df)
