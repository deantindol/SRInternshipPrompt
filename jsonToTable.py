import pandas as pd
import json

jsonString = "" #json string to be parsed into table
    
data = json.loads(jsonString)
teams = list(data.keys())
numTeams = len(teams)

winsLosses = [[0] * numTeams for i in range(numTeams)]
for i in range(numTeams):
    for j in range(numTeams):
        if i == j:
            winsLosses[i][j] = "-"
        else:
            winsLosses[i][j] = data[teams[i]][teams[j]]["W"]

df = pd.DataFrame(winsLosses, index=teams, columns=teams)

print(df)

