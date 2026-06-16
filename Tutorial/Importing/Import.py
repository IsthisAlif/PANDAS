import pandas as pd

# Import CSV
df1 = pd.read_csv("Tutorial/Importing/pokedex.csv")
print(df1.to_string())

# Import JSON
df2 = pd.read_json("Tutorial/Importing/pokedex.json")
print(df2.to_string())