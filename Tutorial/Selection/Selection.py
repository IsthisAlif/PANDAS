import pandas as pd

df = pd.read_csv("Tutorial/Selection/pokedex.csv", index_col="Name") # set column as index

# SELECTION BY COLUMNS
#print(df["Name"].to_string())
#print(df["Type 1"].to_string())
#print(df[["Name", "Type 1", "Type 2"]].to_string())

# SELECTION BY ROWS
#print(df.loc[0])
#print(df.loc["Charizard":"Blastoise", ["Type 1", "Type 2"]])
#print(df.iloc[0:11:2, 0:3])