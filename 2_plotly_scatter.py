import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# set random.seed() so numbers are same as instructor.
np.random.seed(42)
# make a data set.
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)
# testing
print(random_x)
print(random_y)


data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='pentagon',
                       line=dict(width=2)
                    ))]
layout = go.Layout(title='Hello! My First Scatter Plot',
                   xaxis={'title':'MY X AXIS'},     #making a dictionary; one way.
                   yaxis=dict(title='MY Y AXIS'),   #making a dictionary; another way. Plotly docs uses this convention.
                   hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter.html')
