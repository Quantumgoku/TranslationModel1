import pandas as pd
data =pd.read_csv('DataSetR.csv')

df = pd.DataFrame(data)
df_unique_english = df.drop_duplicates(subset=['English'])

df_unique_english=df_unique_english.dropna()

df_unique_english.to_csv('DataSetR.csv', index=False)