import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/2018WinterOlympics.csv')
#print(df)

data = [go.Bar(x=df['NOC'],
               y=df['Total'])]

layout = go.Layout(title='Medals 2018 Winter Olympics')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)