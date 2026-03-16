import pandas as pd
data={ "name": ["a","b","c","d"],
       "age" : [25, None , 30,20],
       "salary" : [5000,6000,None, 3000]
     }
df = pd.DataFrame(data)
print("original data")
print(df)
df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)
print("After wrangling")
print(df)
