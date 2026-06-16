import pandas as pd

df = pd.read_csv("Exersice/Exercise 1/pokedex.csv", index_col="Name") # set column as index

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")