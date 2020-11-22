import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')
# print(df)

data = [go.Scatter(x=df['horsepower'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight'] / 100,
                               color=df['cylinders'],
                               showscale=True)
                   )]

layout = go.Layout(title='Bubble Chart',
                   xaxis=dict(
                       title='Horsepower',
                   ),
                   yaxis=dict(
                       title="Acceleration in Seconds"
                   ),
                   hovermode='closest'
                   )

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='mpg_bubble_chart.html')
