import pandas as pd

# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1-Dimensional)

#data = [100, 102, 104, 200, 202]

#series = pd.Series(data, index=["a", "b", "c", "d", "e"])

#print(series)
#series.loc["c"] = 200
#print(series.iloc[0])
#print(series[series < 200])

calories = {"Day 1" : 1750,
            "Day 2" : 2100,
            "Day 3" : 1700}

series = pd.Series(calories)
#series.loc["Day 3"] += 500
print(series[series < 2000])