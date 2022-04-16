import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")

fig = ff.create_distplot([list(data["Avg Rating"])], ["Mobile Brands"])
fig.show()
