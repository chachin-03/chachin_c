from sklearn.preprocessing import MinMaxScaler
import pandas as pd
data ={"salary" : [25000,30000,28000,36000]}
df=pd.DataFrame(data)
scaler = MinMaxScaler()
df["Normalized"]=scaler.fit_transform(df[["salary"]])
print(df)
