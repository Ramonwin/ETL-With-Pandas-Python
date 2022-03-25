import pandas as pd
df_participant = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqthon-participants.csv')

df_participant['postal_code'] = df_participant['address'].str.extract(r'(\d+)$')
print(df_participant['postal_code'])