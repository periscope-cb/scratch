import pandas as pd

df_sfdc = pd.read_csv("salesforce.csv")
df = pd.read_csv("dedupe.csv")

df["in_sfdc"] = df["website"].isin(df_sfdc["WEBSITE"])

<<<<<<< HEAD
df.to_csv('dedupe_output.csv', index=False)
=======
df.to_csv("dedupe_output.csv")
>>>>>>> 86ca18654f48be1394af1656b5fafe95f00b29fb
