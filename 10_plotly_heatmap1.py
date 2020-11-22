import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/2010SantaBarbaraCA.csv')
print(df)
print(df.columns)

# z axis is the colorscale.
data = [go.Heatmap(x=df['DAY'],
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'],
                   colorscale='Jet')]


layout = go.Layout(title='SantaBarbara Temps')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='SB_temp_plot.html')