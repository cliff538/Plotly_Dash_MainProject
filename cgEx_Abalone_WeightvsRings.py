import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/abalone.csv')
# print(df)

data = [go.Scatter(x=df['shell_weight'],
                   y=df['rings'],
                   text=df['diameter'],
                   mode='markers',
                   # marker=dict(size=df['shell_weight'] * 10,
                   #             color=df['rings'],
                   #             showscale=True)
                   )]

layout = go.Layout(title='Shell Weight vs Rings',
                   xaxis=dict(
                       title='Shell Weight',
                   ),
                   yaxis=dict(
                       title="Rings"
                   ),
                   hovermode='closest'
                   )

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='shell_weight_rings.html')