import pandas as pd

# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1-Dimensional)

#data = [100, 102, 104, 200, 202]

#series = pd.Series(data, index=["a", "b", "c", "d", "e"])

#print(series)
#series.loc["c"] = 200
#print(series.iloc[0])
#print(series[series < 200])

pokemon = {1 : "Bulbasaur",
            2 : "Ivysaur",
            3 : "Venusaur",
            4 : "Charmander",
            5 : "Charmeleon",
            6 : "Charizard",
            7 : "Squirtle",
            8 : "Wartortle",
            9 : "Blastoise"}

series = pd.Series(pokemon)
#series.loc["Day 3"] += 500
print(series)