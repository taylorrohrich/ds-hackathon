# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
data = pd.read_csv("covid.csv")
print(data.head())


# %%

# columns of interest: total_cases_per_million

parsedData = data[["location", "date", "total_cases_per_million"]]
parsedData = parsedData.loc[(parsedData['location'] ==
                             "World") | (parsedData['location'] == "United Kingdom") | (parsedData['location'] ==
                                                                                        "United States") | (parsedData['location'] ==
                                                                                                            "South Korea") | (parsedData['location'] ==
                                                                                                                              "China"), ]
parsedData['date'] = pd.to_datetime(parsedData['date'])
threeMonths = datetime.date.today() - datetime.timedelta(days=90)
parsedData = parsedData[(parsedData['date'] > np.datetime64(threeMonths))]
# %%

# matplotlib
print(threeMonths)
xCoords = parsedData.loc[parsedData['location'] == 'World', 'date']
yCoords = parsedData.loc[parsedData['location']
                         == 'World', 'total_cases_per_million']
plt.plot(xCoords, yCoords)


# %%
