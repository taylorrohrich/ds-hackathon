# %%
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
data = pd.read_csv("covid.csv")

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
plt.title('Total confirmed COVID-19 cases per million people')
plt.xlabel('Date')
plt.ylabel('Log')
locations = ['World', 'United States',
             'United Kingdom', 'South Korea', 'China']
patches = []
color = ['red', 'green', 'blue', 'orange', 'yellow']
for i, location in enumerate(locations):
    xCoords = parsedData.loc[parsedData['location'] == location, 'date']
    yCoords = parsedData.loc[parsedData['location']
                             == location, 'total_cases_per_million']
    plt.plot(xCoords, yCoords, color=color[i])
    patches.append(mpatches.Patch(color=color[i], label=location))
plt.yscale('log')
plt.legend(handles=patches)

# %%


df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],  # Spatial coordinates
    z=df['total exports'].astype(float),  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    colorbar_title="Millions USD",
))

fig.update_layout(
    title_text='2011 US Agriculture Exports by State',
    geo_scope='usa',  # limite map scope to USA
)

fig.show()


# %%
df = data[["location", "iso_code",
           "date", "total_cases_per_million"]]
df['date'] = pd.to_datetime(df['date'])
yesterday = datetime.date.today() - datetime.timedelta(days=1)
df = df[(df['date'] > np.datetime64(yesterday))]

# %%

fig = go.Figure(data=go.Choropleth(
    locations=df['iso_code'],
    z=df["total_cases_per_million"],
    text=df['location'],
    colorscale='Reds',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    # colorbar_ticksuffix='(millions)',
    colorbar_title='Total confirmed COVID-19 cases per million people',
))

fig.update_layout(
    title_text='Total confirmed COVID-19 cases per million people',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
)

fig.show()
