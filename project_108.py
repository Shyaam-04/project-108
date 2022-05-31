import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data_108P.csv")
data = df["Avg Rating"].tolist()

fig = ff.create_distplot([data],["Average Rating of amazon products"])
fig.show()