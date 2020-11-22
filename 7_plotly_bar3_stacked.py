import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

"""
No loop required, simple bar chart with static data that isn't being tracked across a time frame. 
This is called a Stacked Bar Chart. 
Only difference between Nested Bar Chart is adding conditon barmode='stack' to layout. 
"""


df = pd.read_csv('data/2018WinterOlympics.csv')
#print(df)

trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold',
                marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker={'color':'#CD7F32'})


data = [trace1, trace2, trace3]
layout = go.Layout(title='Medals 2018 Winter Olympics', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stacked_bar_chart.html')

print(trace1)