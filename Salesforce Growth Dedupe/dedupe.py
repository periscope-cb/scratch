import pandas as pd

df_sfdc = pd.read_csv('salesforce.csv')
df = pd.read_csv('dedupe.csv')

df['in_sfdc'] = df['website'].isin(df_sfdc['WEBSITE'])

df.to_csv('dedupe_output.csv', index=False)