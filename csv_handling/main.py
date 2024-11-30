import pandas as pd

df = pd.read_csv("csv/zyada_bada_data.csv")
print(df)

df.to_csv("csv/naya_csv.csv")